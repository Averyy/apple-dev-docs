# Image

**Framework**: Maps Web Snapshots  
**Kind**: dict

A JSON object for a Snapshot URL that describes the characteristics of custom images to use for map annotations.

**Availability**:
- Maps Web Snapshots 1.0+ (Beta)

#### Discussion

Maps Web Snapshots API supports JPEG, PNG, and GIF image formats for providing custom annotations. You may use up to 10 unique images in a snapshot request, and you may use an image for more than one annotation. It’s a good idea to use a URL shortener for image URLs so you don’t exceed the maximum character limit for a Snapshots URL.

If an image fails to load in a reasonable amount of time, the snapshot rendering uses the default “balloon” style marker.

> ❗ **Important**: By providing an image URL, you’re responsible for ensuring the availability of the image at all times.

By providing an image URL, you’re responsible for ensuring the availability of the image at all times.

## See Also

- [Generating a URL and Signature to Create a Maps Web Snapshot](generating_a_url_and_signature_to_create_a_maps_web_snapshot.md)
  Create a Snapshot URL and generate a signature to validate the request. 
- [object Annotation](annotation.md)
  An object for a Snapshot URL that describes annotation characteristics.
- [object Overlay](overlay.md)
  A JSON object for a Snapshot URL that describes overlay shape characteristics, including points for the overlay and styles such as width, color, and dash pattern.
- [object OverlayStyle](overlaystyle.md)
  A  JSON object that describes reusable styles for an overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/snapshots/image)*