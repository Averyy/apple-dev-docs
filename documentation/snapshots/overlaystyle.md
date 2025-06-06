# OverlayStyle

**Framework**: Maps Web Snapshots  
**Kind**: dict

A  JSON object that describes reusable styles for an overlay.

**Availability**:
- Maps Web Snapshots 1.0+ (Beta)

#### Discussion

You pass the `OverlayStyle` object properties from the `overlayStyles` query parameter. You can set the object properties and reuse the styles for multiple objects. Any changes made to an `OverlayStyle` object property automatically changes the styles associated with that object, unless they’re overwritten using the `Overlay` object. 

The following example shows `OverlayStyle` properties passed into the `overlayStyles` query parameter:

```other
/snapshot?center=0,0&z=7&overlays=[{
"type": "polygon",
"points":["1,1","1,-1","-1,-1","-1,1"],
"styleIdx": 2
}]
&overlayStyles=[{
"fillColor": "teal",
"fillOpacity": 0.7,
"strokeColor": "blue",
"lineCap": "square",
"lineWidth": 11,
"strokeOpacity": 0.7 }]
```

## Topics

### Objects
- [object OverlayStyle.LineGradient](overlaystyle/linegradient.md)
  A property that sets the color stops for the gradient, positioned by offsets between 0 and 1.
- [object OverlayStyle.LineGradientIndexes](overlaystyle/linegradientindexes.md)
  A property that sets the color stops for the gradient, positioned by indexes of points on the polyline.

## See Also

- [Generating a URL and Signature to Create a Maps Web Snapshot](generating_a_url_and_signature_to_create_a_maps_web_snapshot.md)
  Create a Snapshot URL and generate a signature to validate the request. 
- [object Annotation](annotation.md)
  An object for a Snapshot URL that describes annotation characteristics.
- [object Overlay](overlay.md)
  A JSON object for a Snapshot URL that describes overlay shape characteristics, including points for the overlay and styles such as width, color, and dash pattern.
- [object Image](image.md)
  A JSON object for a Snapshot URL that describes the characteristics of custom images to use for map annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/snapshots/overlaystyle)*