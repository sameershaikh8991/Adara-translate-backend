import traceback
import whisper
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import JsonResponse

class ProcessAudioView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        audio_file = request.FILES.get('audio')
        if not audio_file:
            return Response({"error": "No audio file provided."}, status=400)

        try:
            # Save file temporarily
            temp_file_path = f"/tmp/{audio_file.name}"
            with open(temp_file_path, 'wb') as temp_file:
                for chunk in audio_file.chunks():
                    temp_file.write(chunk)

            # Initialize whisper model
            model = whisper.load_model("base", device="cpu")  # Ensure it's using CPU

            # Transcribe the audio
            result = model.transcribe(temp_file_path)

            # Clean up after transcription
            os.remove(temp_file_path)

            return Response({"transcription": result['text']})

        except Exception as e:
            # Log the full exception traceback for debugging
            error_details = traceback.format_exc()
            print(f"Error processing the audio: {error_details}")

            return JsonResponse({
                "error": "An error occurred during transcription.",
                "details": str(e),
                "traceback": error_details
            }, status=500)
