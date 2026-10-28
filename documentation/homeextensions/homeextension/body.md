# body

**Framework**: HomeExtensions  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The content that your extension provides to the Home app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@ContentBuilder
@MainActor var body: Self.Content { get }
```

## Discussion

For example, to provide a configuration view:

```swift
var body: some HomeContent {
    HomeAccessoryConfiguration(id: "my-config") {
        ConfigurationFeaturesView()
    }
}
```

## See Also

### Providing content
- [associatedtype Content : HomeContent](./content.md)
  The type of content that your extension provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeextension/body)*