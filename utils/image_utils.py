import base64


def image_to_base64(uploaded_file):

    bytes_data = uploaded_file.read()

    base64_image = base64.b64encode(bytes_data).decode("utf-8")

    return base64_image