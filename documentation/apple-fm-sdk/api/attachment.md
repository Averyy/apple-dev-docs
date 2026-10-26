---
source: apple-fm-sdk
framework: apple-fm-sdk
url: https://apple.github.io/python-apple-fm-sdk/api/attachment.html
---

# Attachment

This page documents the Attachment classes for passing images to a model.

Note

**Swift Equivalent:** This Python API corresponds to the [Attachment](https://developer.apple.com/documentation/foundationmodels/attachment) protocol in the Swift Foundation Models Framework.

## Attachment Class

**class apple_fm_sdk.Attachment**
: Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)
Represents an attachment passed to a prompt with an optional label.
Attachments allow you to include non-text content (such as images) in your
prompts. The model can process these attachments as part of the input context.
Use the optional `label` parameter to allow the model to reference this
attachment by name, which is particularly useful when the model needs to call
tools that reference specific attachments. When omitted, the attachment is
added without a label.

Note
This is an abstract base class. Use concrete implementations like
[ImageAttachment](#apple_fm_sdk.ImageAttachment) to create actual attachments.

See also

[ImageAttachment](#apple_fm_sdk.ImageAttachment): For attaching images to prompts

abstractmethod add_to_composed_prompt(*composed_prompt*)
Add this attachment to a composed prompt.
This internal method is called by the framework to add the attachment
to the native prompt representation.

Parameters:
**composed_prompt** (*ctypes pointer*) – The native composed prompt object to add this attachment to

Raises:
[ImagePromptError](#apple_fm_sdk.ImagePromptError) – If the attachment cannot be added

## ImageAttachment Class

**class apple_fm_sdk.ImageAttachment**
: Bases: [Attachment](#apple_fm_sdk.Attachment)
Represents an image attachment passed to a prompt with an optional label.
Image attachments enable multimodal prompts by allowing you to include images
alongside text in your prompts. The model can analyze and reference these images
when generating responses.
When you provide a `label`, the model can reference the image by name, which is
particularly useful for:

Distinguishing between multiple images in a single prompt
Allowing tools to reference specific images
Providing context about what each image represents

Variables:

**_path** (*Path*) – Path to the image file on disk
**_label** (*Optional**[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]*) – Optional label for the image

Examples
Basic image attachment:

  ```
  import apple_fm_sdk as fm
  from pathlib import Path

  session = fm.LanguageModelSession()
  image = fm.ImageAttachment(Path("photo.jpg"))
  response = await session.respond(["What's in this image?", image])
  ```

Labeled image attachment:

  ```
  import apple_fm_sdk as fm
  from pathlib import Path

  session = fm.LanguageModelSession()
  diagram = fm.ImageAttachment(Path("diagram.png"), label="architecture")
  response = await session.respond([
      "Explain the architecture shown in the diagram",
      diagram
  ])
  ```

Multiple images with labels:

  ```
  import apple_fm_sdk as fm
  from pathlib import Path

  session = fm.LanguageModelSession()
  before = fm.ImageAttachment(Path("before.jpg"), label="before")
  after = fm.ImageAttachment(Path("after.jpg"), label="after")
  response = await session.respond([
      "Compare the before and after images",
      before,
      after
  ])
  ```

See also

[Attachment](#apple_fm_sdk.Attachment): Base class for all attachment types
[LanguageModelSession](session.md#apple_fm_sdk.LanguageModelSession): For using attachments in sessions

Note
The image file must exist at the specified path when the attachment is created.
Supported image formats depend on the underlying model capabilities.

__init__(*path*, *label=None*)
Create an image attachment for use in prompts.

Parameters:

**path** (*Path*) – Path on disk to the image file to attach. The file must exist
at this location when the attachment is created.
**label** (*Optional**[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]*) – Optional label for the attachment. Use this to allow the model
to reference the image by name, particularly useful when working with
multiple images or when tools need to reference specific images.

Raises:
[ImagePromptError](#apple_fm_sdk.ImagePromptError) – If the file does not exist at the specified path

Example:

  ```
  import apple_fm_sdk as fm
  from pathlib import Path

  # Create an unlabeled image attachment
  image = fm.ImageAttachment(Path("photo.jpg"))

  # Create a labeled image attachment
  diagram = fm.ImageAttachment(Path("diagram.png"), label="system_diagram")
  ```

add_to_composed_prompt(*composed_prompt*)
Add this image attachment to a composed prompt.
This internal method is called by the framework to add the image attachment
to the native prompt representation. It handles encoding the file path and
optional label, then calls the C binding to attach the image.

Parameters:
**composed_prompt** (*ctypes pointer*) – The native composed prompt object to add this attachment to

Raises:
[ImagePromptError](#apple_fm_sdk.ImagePromptError) – If the attachment cannot be added, either because
the image format is not supported or another error occurs

## PromptError Class

**class apple_fm_sdk.PromptError**
: Bases: [Exception](https://docs.python.org/3/library/exceptions.html#Exception)
Base exception for prompt-related errors.
This exception is raised when there are issues with prompt construction or
processing, such as invalid prompt components or failures in adding attachments.

See also

[ImagePromptError](#apple_fm_sdk.ImagePromptError): Specific error type for image attachment issues

## ImagePromptError Class

**class apple_fm_sdk.ImagePromptError**
: Bases: [PromptError](#apple_fm_sdk.PromptError)
Exception raised for errors specific to image prompts.
This exception is raised when there are issues with image attachments, such as:

Image file not found at the specified path
Unsupported image format
Failure to add the image to the prompt

Examples
Handling image prompt errors:

  ```
  import apple_fm_sdk as fm
  from pathlib import Path

  try:
      image = fm.ImageAttachment(Path("nonexistent.jpg"))
  except fm.ImagePromptError as e:
      print(f"Failed to create image attachment: {e}")

  try:
      session = fm.LanguageModelSession()
      response = await session.respond([
          "Describe this image:",
          fm.ImageAttachment(Path("photo.jpg"))
      ])
  except fm.ImagePromptError as e:
      print(f"Failed to process image prompt: {e}")
  ```

See also

[PromptError](#apple_fm_sdk.PromptError): Base class for all prompt errors
[ImageAttachment](#apple_fm_sdk.ImageAttachment): For creating image attachments
