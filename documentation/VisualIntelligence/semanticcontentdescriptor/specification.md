# SemanticContentDescriptor.Specification

**Framework**: Visual Intelligence  
**Kind**: typealias

A type that specifies how the system resolves a semantic content descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
typealias Specification = some ResolverSpecification
```

#### Discussion

This type is part of the internal mechanism that App Intents uses to process visual intelligence data. It defines the specification type that determines how the system resolves a [`SemanticContentDescriptor`](semanticcontentdescriptor.md) instance.

## See Also

- [static var defaultResolverSpecification: some ResolverSpecification](semanticcontentdescriptor/defaultresolverspecification.md)
  A default implementation of an internal type that the App Intents framework uses to convert data values with resolvers.
- [SemanticContentDescriptor.ValueType](semanticcontentdescriptor/valuetype.md)
  A type that represents the value of a semantic content descriptor.
- [SemanticContentDescriptor.UnwrappedType](semanticcontentdescriptor/unwrappedtype.md)
  A type that represents the unwrapped value of a semantic content descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visualintelligence/semanticcontentdescriptor/specification)*