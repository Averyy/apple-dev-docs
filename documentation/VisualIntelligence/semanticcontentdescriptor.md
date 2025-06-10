# SemanticContentDescriptor

**Framework**: Visual Intelligence  
**Kind**: struct

A type that represents a scene that visual intelligence captures, like a screenshot, photo, or photo and video stream.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
struct SemanticContentDescriptor
```

## Mentions

- [Integrating your app with visual intelligence](integrating-your-app-with-visual-intelligence.md)

## Topics

### Accessing semantic content
- [let labels: [String]](semanticcontentdescriptor/labels.md)
  A list of labels that visual intelligence uses to classify items onscreen or visual intelligence camera.
- [var pixelBuffer: CVReadOnlyPixelBuffer?](semanticcontentdescriptor/pixelbuffer.md)
  The pixel buffer that visual intelligence captures.
### Protocol conformance
- [static var defaultResolverSpecification: some ResolverSpecification](semanticcontentdescriptor/defaultresolverspecification.md)
  A default implementation of an internal type that the App Intents framework uses to convert data values with resolvers.
- [SemanticContentDescriptor.Specification](semanticcontentdescriptor/specification.md)
- [SemanticContentDescriptor.ValueType](semanticcontentdescriptor/valuetype.md)
- [SemanticContentDescriptor.UnwrappedType](semanticcontentdescriptor/unwrappedtype.md)
### Default Implementations
- [CustomStringConvertible Implementations](semanticcontentdescriptor/customstringconvertible-implementations.md)
- [InstanceDisplayRepresentable Implementations](semanticcontentdescriptor/instancedisplayrepresentable-implementations.md)
- [PersistentlyIdentifiable Implementations](semanticcontentdescriptor/persistentlyidentifiable-implementations.md)
- [TypeDisplayRepresentable Implementations](semanticcontentdescriptor/typedisplayrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DisplayRepresentable](../AppIntents/DisplayRepresentable.md)
- [InstanceDisplayRepresentable](../AppIntents/InstanceDisplayRepresentable.md)
- [PersistentlyIdentifiable](../AppIntents/PersistentlyIdentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](../AppIntents/TypeDisplayRepresentable.md)

## See Also

- [Integrating your app with visual intelligence](integrating-your-app-with-visual-intelligence.md)
  Enable people to find app content that matches their surroundings or objects onscreen with visual intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visualintelligence/semanticcontentdescriptor)*