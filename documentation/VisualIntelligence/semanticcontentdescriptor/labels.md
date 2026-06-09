# labels

**Framework**: Visual Intelligence  
**Kind**: property

A list of labels that visual intelligence uses to classify items onscreen or in visual intelligence camera.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
let labels: [String]
```

## Mentions

- [Integrating your app with visual intelligence](integrating-your-app-with-visual-intelligence.md)

#### Discussion

The Visual Intelligence framework defines the possible label values. Use them to search for content in your app and return matching content to visual search.

> **Note**: Labels are general, high-level terms in the `en_US` locale and might change over time. The Visual Intelligence framework doesn’t translate them or include synonyms. For example, `SemanticContentDescriptor` might provide the labels `tower` or `building` for a well-known building. It won’t provide the building’s actual name as a label.

## See Also

- [var pixelBuffer: CVReadOnlyPixelBuffer?](semanticcontentdescriptor/pixelbuffer.md)
  The pixel buffer that visual intelligence captures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visualintelligence/semanticcontentdescriptor/labels)*