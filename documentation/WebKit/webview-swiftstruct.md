# WebView

**Framework**: WebKit  
**Kind**: struct

A view that displays some web content.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency struct WebView
```

#### Overview

Present HTML, CSS, and JavaScript content alongside your app’s native views with [`WebView`](webview-swift.struct.md). Specify web content with a [`URL`](https://developer.apple.com/documentation/Foundation/URL) when using the [`init(url:)`](webview-swift.struct/init(url:).md) initializer, or with a [`WebPage`](webpage.md) when using the [`init(_:)`](webview-swift.struct/init(_:).md) initializer, which allows you to fully control the browsing experience. Any updates to the page propagate the information to the view.

[`WebView`](webview-swift.struct.md) provides a complete browsing experience, including the ability to navigate between different webpages using links, forward and back buttons, and more. When a person clicks a link in your content, the view acts like a browser and displays the content at that link. To customize navigation, use a [`WebPage`](webpage.md) with your [`WebView`](webview-swift.struct.md) and customize the [`WebPage.Configuration`](webpage/configuration.md), or create a new type that conforms to [`WebPage.NavigationDeciding`](webpage/navigationdeciding.md).

The following example displays two different URLs depending on the state of a toggle, and also prevents back-forward navigation gestures:

```swift
struct ContentView: View {
    @State private var toggle = false

    private var url: URL? {
        toggle ? URL(string: "https://www.webkit.org") : URL(string: "https://www.swift.org")
    }

    var body: some View {
        WebView(url: url)
            .toolbar {
                Button(buttonName, systemImage: buttonIcon) {
                    toggle.toggle()
                }
            }
            .webViewBackForwardNavigationGestures(.disabled)
    }
}
```

A [`WebView`](webview-swift.struct.md) is a scrollable view, and behaves similarly to [`ScrollView`](https://developer.apple.com/documentation/SwiftUI/ScrollView). Customize scrolling in a [`WebView`](webview-swift.struct.md) with:

- [`scrollBounceBehavior(_:axes:)`](https://developer.apple.com/documentation/SwiftUI/View/scrollBounceBehavior(_:axes:))
- [`webViewScrollInputBehavior(_:for:)`](https://developer.apple.com/documentation/SwiftUI/View/webViewScrollInputBehavior(_:for:))
- [`webViewScrollPosition(_:)`](https://developer.apple.com/documentation/SwiftUI/View/webViewScrollPosition(_:))
- [`webViewOnScrollGeometryChange(for:of:action:)`](https://developer.apple.com/documentation/SwiftUI/View/webViewOnScrollGeometryChange(for:of:action:))

Customize [`WebView`](webview-swift.struct.md) display and interactions with view modifiers, such as:

- [`webViewBackForwardNavigationGestures(_:)`](https://developer.apple.com/documentation/SwiftUI/View/webViewBackForwardNavigationGestures(_:))
- [`webViewMagnificationGestures(_:)`](https://developer.apple.com/documentation/SwiftUI/View/webViewMagnificationGestures(_:))
- [`webViewLinkPreviews(_:)`](https://developer.apple.com/documentation/SwiftUI/View/webViewLinkPreviews(_:))
- [`webViewTextSelection(_:)`](https://developer.apple.com/documentation/SwiftUI/View/webViewTextSelection(_:))
- [`webViewElementFullscreenBehavior(_:)`](https://developer.apple.com/documentation/SwiftUI/View/webViewElementFullscreenBehavior(_:))
- [`webViewContextMenu(menu:)`](https://developer.apple.com/documentation/SwiftUI/View/webViewContextMenu(menu:))
- [`webViewContentBackground(_:)`](https://developer.apple.com/documentation/SwiftUI/View/webViewContentBackground(_:))

To further customize and control a web interaction, connect a [`WebView`](webview-swift.struct.md) to a [`WebPage`](webpage.md). The following example demonstrates this by configuring the view’s navigation title to be the webpage’s title, which the system updates automatically because [`WebPage`](webpage.md) is an `Observable` type:

```swift
struct ContentView: View {
    @State private var page = WebPage()

    var body: some View {
        NavigationStack {
            WebView(page)
                .navigationTitle(page.title)
        }
    }
}
```

You can only bind a [`WebPage`](webpage.md) to a single [`WebView`](webview-swift.struct.md) at a time.

## Topics

### Creating web views
- [init(WebPage)](webview-swift.struct/init(_:).md)
  Create a new WebView.
- [init(url: URL?)](webview-swift.struct/init(url:).md)
  Create a new WebView with the specified URL.
### Modifying web interactions
- [WebView.BackForwardNavigationGesturesBehavior](webview-swift.struct/backforwardnavigationgesturesbehavior.md)
  A type that defines the behavior of how horizontal swipe gestures trigger backward and forward page navigation.
- [WebView.LinkPreviewBehavior](webview-swift.struct/linkpreviewbehavior.md)
  A type specifying the behavior for the presentation of link previews when pressing a link.
### Structures
- [WebView.ActivatedElementInfo](webview-swift.struct/activatedelementinfo.md)
  Contains information about an element the user activated in a webpage, which may be used to configure a context menu for that element.
- [WebView.ElementFullscreenBehavior](webview-swift.struct/elementfullscreenbehavior.md)
  The behavior that determines whether a web view can display content full screen.
- [WebView.MagnificationGesturesBehavior](webview-swift.struct/magnificationgesturesbehavior.md)
  The options for controlling the behavior for how magnification gestures interact with web views.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [class WebPage](webpage.md)
  An object that controls and manages the behavior of interactive web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.struct)*