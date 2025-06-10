# RelevanceEntriesProviderContext

**Framework**: WidgetKit  
**Kind**: struct

An object that contains details about how a widget is rendered, including its size.

**Availability**:
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct RelevanceEntriesProviderContext
```

## Topics

### Instance Properties
- [let displaySize: CGSize](relevanceentriesprovidercontext/displaysize.md)
  The size, in points, of the widget.
- [let isPreview: Bool](relevanceentriesprovidercontext/ispreview.md)
  A Boolean value that indicates when the widget appears as a preview-only.

## See Also

- [func entry(configuration: Self.Configuration, context: Self.Context) async throws -> Self.Entry](relevanceentriesprovider/entry(configuration:context:).md)
  Provides the entry used to render a widget for a specific relevance configuration.
- [func relevance() async -> WidgetRelevance<Self.Configuration>](relevanceentriesprovider/relevance.md)
  Provides a collection of conditions under which a specific widget could be relevant.
- [func placeholder(context: Self.Context) -> Self.Entry](relevanceentriesprovider/placeholder(context:).md)
  Provides the entry representing a placeholder version of the widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/relevanceentriesprovidercontext)*