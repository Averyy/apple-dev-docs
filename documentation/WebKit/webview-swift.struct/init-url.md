# init(url:)

**Framework**: WebKit  
**Kind**: init

Create a new WebView with the specified URL.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency init(url: URL?)
```

#### Discussion

For example, you can create a WebView that displays one of two URLs depending on the state of a toggle:

```None
struct URLView: View {
    @State private var url: URL? = nil
    @State private var toggle = false

    var body: some View {
        VStack {
            Button("Toggle") {
                toggle.toggle()
            }
            WebView(url: url)
        }
        .onChange(of: toggle, initial: true) {
            url = toggle ? URL(string: "https://www.webkit.org") : URL(string: "https://www.apple.com")
        }
    }
}
```

## Parameters

- `url`: The URL to display in the view. If this value is non-nil or changes to become a non-nil value, the new URL is loaded into the view.

## See Also

- [init(WebPage)](webview-swift.struct/init(_:).md)
  Create a new WebView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.struct/init(url:))*