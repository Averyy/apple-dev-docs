# SemanticContentDescriptor

**Framework**: Visual Intelligence  
**Kind**: struct  
**Role**: Structure

A type that represents a scene that visual intelligence captures, for example, a screenshot, photo, or photo and video stream.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS

## Declaration

```swift
struct SemanticContentDescriptor
```

## Mentions

- [Integrating your app with visual intelligence](./integrating-your-app-with-visual-intelligence.md)

## Topics

### Accessing semantic content
- [let labels: [String]](./semanticcontentdescriptor/labels.md)
  A list of labels that visual intelligence uses to classify items onscreen or in visual intelligence camera.
- [var pixelBuffer: CVReadOnlyPixelBuffer?](./semanticcontentdescriptor/pixelbuffer.md)
  The pixel buffer that visual intelligence captures.
### Protocol conformance
- [static var defaultResolverSpecification: some ResolverSpecification](./semanticcontentdescriptor/defaultresolverspecification.md)
  A default implementation of an internal type that the App Intents framework uses to convert data values with resolvers.
- [SemanticContentDescriptor.Specification](./semanticcontentdescriptor/specification.md)
  A type that specifies how the system resolves a semantic content descriptor.
- [SemanticContentDescriptor.ValueType](./semanticcontentdescriptor/valuetype.md)
  A type that represents the value of a semantic content descriptor.
- [SemanticContentDescriptor.UnwrappedType](./semanticcontentdescriptor/unwrappedtype.md)
  A type that represents the unwrapped value of a semantic content descriptor.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/customlocalizedstringresourceconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [DisplayRepresentable](../AppIntents/displayrepresentable.md)
- [Encodable](../Swift/encodable.md)
- [Escapable](../Swift/escapable.md)
- [InstanceDisplayRepresentable](../AppIntents/instancedisplayrepresentable.md)
- [IntentValueConvertible](../AppIntents/intentvalueconvertible.md)
- [IntentValueExpressing](../AppIntents/intentvalueexpressing.md)
- [PersistentlyIdentifiable](../AppIntents/persistentlyidentifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TypeDisplayRepresentable](../AppIntents/typedisplayrepresentable.md)

## See Also

### Search integration
- [Integrating your app with visual intelligence](./integrating-your-app-with-visual-intelligence.md)
  Enable people to find app content that matches their surroundings or objects onscreen with visual intelligence.
- [Adopting App Intents to support system experiences](../AppIntents/adopting-app-intents-to-support-system-experiences.md)
  Create app intents and entities so people can use your app’s content and actions across system experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visualintelligence/semanticcontentdescriptor)*