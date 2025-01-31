import torch
import soundfile as sf


def text_to_audio(gpt_response: str):
    text = f'<speak><prosody rate="slow">{gpt_response}</prosody></speak>'
    language = 'ru'
    model_id = 'v4_ru'
    device = torch.device('cpu')

    model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                         model='silero_tts',
                                         language=language,
                                         speaker=model_id)
    model.to(device)
    sample_rate = 48000
    speaker = 'eugene'
    put_accent = True
    put_yo = True

    audio = model.apply_tts(ssml_text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    audio_np = audio.numpy()
    with sf.SoundFile("output.wav", 'w', samplerate=48000, channels=1) as file:
        file.write(audio_np)
