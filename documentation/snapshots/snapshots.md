# Maps Web Snapshots

**Framework**: Maps Web Snapshots

Create a static image of a map from a URL.

**Availability**:
- Maps Web Snapshots 1.0+ (Beta)

#### Overview

Use the Maps Web Snapshots service to generate static map images from a URL. You can use Snapshots any time that an interactive map isn’t required, and in any place you typically use an image URL — in web pages, and in places where JavaScript isn’t available, such as email clients.

![A screenshot of a  map created using Maps Web Snapshots API.](https://docs-assets.developer.apple.com/published/19ae23841c/3325414@2x.png)

> **Note**: If you need an interactive map on the web, see [`MapKit JS`](https://developer.apple.com/documentation/mapkitjs). To generate static map snapshots in iOS, macOS, or tvOS apps, see [`MKMapSnapshotter`](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter).

If you need an interactive map on the web, see [`MapKit JS`](https://developer.apple.com/documentation/mapkitjs). To generate static map snapshots in iOS, macOS, or tvOS apps, see [`MKMapSnapshotter`](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter).

To learn how to construct a signed and validated snapshot URL, see [`Generating a URL and Signature to Create a Maps Web Snapshot`](generating_a_url_and_signature_to_create_a_maps_web_snapshot.md). You generate the required signature using credentials obtained through your Apple Developer account. See [`Creating a Maps identifier and a private key`](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key) to learn how to get these credentials. You can also obtain HTML to show information about a place using [`Create a Map`](https://developer.apple.comhttps://devcms.apple.com/maps/create-a-map/).

For more information on usage limits for Maps Web Snapshots, see the Apple Developer page, [`Maps on the Web`](https://developer.apple.comhttps://developer.apple.com/maps/web/).

## Topics

### Essentials
- [Generating a URL and Signature to Create a Maps Web Snapshot](generating_a_url_and_signature_to_create_a_maps_web_snapshot.md)
  Create a Snapshot URL and generate a signature to validate the request. 
- [object Annotation](annotation.md)
  An object for a Snapshot URL that describes annotation characteristics.
- [object Overlay](overlay.md)
  A JSON object for a Snapshot URL that describes overlay shape characteristics, including points for the overlay and styles such as width, color, and dash pattern.
- [object OverlayStyle](overlaystyle.md)
  A  JSON object that describes reusable styles for an overlay.
- [object Image](image.md)
  A JSON object for a Snapshot URL that describes the characteristics of custom images to use for map annotations.
### Snapshots
- [Create a Maps Web Snapshot](create_a_maps_web_snapshot.md)
  Generates a map image with characteristics that you provide in the query parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/snapshots)*