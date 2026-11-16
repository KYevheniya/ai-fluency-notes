"""Fetch YouTube captions for every lesson in lessons.json.

Writes transcripts/NN-slug.md per lesson: the lesson page text first
(objectives, takeaways, exercises), then the full video transcript as
paragraphs with [mm:ss] markers.

Usage: .venv/bin/python fetch_transcripts.py [lessons.json]
"""
import json
import re
import sys
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi

PARAGRAPH_SECONDS = 45  # start a new paragraph roughly every 45 s of speech


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def mmss(seconds: float) -> str:
    s = int(seconds)
    return f"{s // 60:02d}:{s % 60:02d}"


def to_paragraphs(snippets) -> str:
    paras, current, start = [], [], None
    for snip in snippets:
        if start is None:
            start = snip.start
        current.append(snip.text.replace("\n", " ").strip())
        ends_sentence = current[-1].endswith((".", "?", "!"))
        if snip.start - start >= PARAGRAPH_SECONDS and ends_sentence:
            paras.append(f"**[{mmss(start)}]** " + " ".join(current))
            current, start = [], None
    if current:
        paras.append(f"**[{mmss(start)}]** " + " ".join(current))
    return "\n\n".join(paras)


def main() -> None:
    lessons_path = Path(sys.argv[1] if len(sys.argv) > 1 else "lessons.json")
    lessons = json.loads(lessons_path.read_text())
    out_dir = lessons_path.parent / "transcripts"
    out_dir.mkdir(exist_ok=True)
    api = YouTubeTranscriptApi()

    for lesson in lessons:
        name = f"{lesson['n']:02d}-{slug(lesson['title'])}.md"
        parts = [
            f"# {lesson['n']:02d}. {lesson['title']}",
            f"Lesson: {lesson['url']}",
        ]
        vid = lesson.get("video_id")
        if vid:
            parts.append(f"Video: https://www.youtube.com/watch?v={vid}")
        parts += ["", "## Lesson page text", "", lesson["page_text"], ""]

        if vid:
            try:
                t = api.fetch(vid, languages=["en"])
                parts += ["## Video transcript", "", to_paragraphs(t.snippets)]
                status = f"{len(t.snippets)} caption lines"
            except Exception as exc:  # keep going, report at the end
                parts += ["## Video transcript", "", f"_Transcript unavailable: {exc}_"]
                status = f"FAILED: {type(exc).__name__}"
        else:
            status = "no video (exercise lesson)"

        (out_dir / name).write_text("\n".join(parts) + "\n")
        print(f"{name:55s} {status}")


if __name__ == "__main__":
    main()
