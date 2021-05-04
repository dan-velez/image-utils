import base64


class ImageBase64:
    """Encode an image into base64."""

    def encode_image(image, voutfile):
        """Encode an image into base64."""
        image_content = image.read()
        return base64.b64encode(image_content)
