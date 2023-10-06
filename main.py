from youtube_transcript_api import YouTubeTranscriptApi
import json


def join_text_values(data):
    # Use a list comprehension to extract the "text" values
    text_values = [item["text"] for item in data if "text" in item]

    # Join the text values into a single string with a space separator
    result_string = ' '.join(text_values)

    return result_string


def download_transcript(video_id, filename):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = join_text_values(transcript)
    with open(f'{filename}.txt', 'w', encoding='utf-8') as file:
        file.write(text)
    return text


def count_words(content):
    words = content.split()
    word_count = len(words)
    return word_count


def count_characters(content):
    char_count = len(content)
    return char_count


def calculateOpenAiGPT3Cost(characters):
    total_tokens = characters / 4
    cost_per_token = 0.0015 / 1000
    return round(total_tokens * cost_per_token, 4)


if __name__ == '__main__':
    text = download_transcript('WCo33G3HT2g', 'T3EmojiApp')
    word_count = count_words(text)
    characters = count_characters(text)
    print(
        f'Done! Word count: {word_count}, character count: {count_characters(text)} approx cost: ${calculateOpenAiGPT3Cost(characters)}')
