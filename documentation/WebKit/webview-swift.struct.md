# WebView

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

A view that displays some web content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency struct WebView
```

#### Overview

Present HTML, CSS, and JavaScript content alongside your app’s native views with [`WebView`](./webview-swift.struct.md). Specify web content with a [`URL`](../Foundation/url.md) when using the [`init(url:)`](./webview-swift.struct/init%28url%29.md) initializer, or with a [`WebPage`](./webpage.md) when using the [`init(_:)`](./webview-swift.struct/init%28_%29.md) initializer, which allows you to fully control the browsing experience. Any updates to the page propagate the information to the view.

[`WebView`](./webview-swift.struct.md) provides a complete browsing experience, including the ability to navigate between different webpages using links, forward and back buttons, and more. When a person clicks a link in your content, the view acts like a browser and displays the content at that link. To customize navigation, use a [`WebPage`](./webpage.md) with your [`WebView`](./webview-swift.struct.md) and customize the [`WebPage.Configuration`](./webpage/configuration.md), or create a new type that conforms to [`WebPage.NavigationDeciding`](./webpage/navigationdeciding.md).

The following example displays two different URLs depending on the state of a toggle, and also prevents back-forward navigation gestures:

```swift
import SwiftUI
import WebKit

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

A [`WebView`](./webview-swift.struct.md) is a scrollable view, and behaves similarly to [`ScrollView`](../SwiftUI/scrollview.md). Customize scrolling in a [`WebView`](./webview-swift.struct.md) with:

- [`scrollBounceBehavior(_:axes:)`](../SwiftUI/view/scrollbouncebehavior%28_,axes%29.md)
- [`webViewScrollInputBehavior(_:for:)`](../SwiftUI/view/webviewscrollinputbehavior%28_,for%29.md)
- [`webViewScrollPosition(_:)`](../SwiftUI/view/webviewscrollposition%28_%29.md)
- [`webViewOnScrollGeometryChange(for:of:action:)`](../SwiftUI/view/webviewonscrollgeometrychange%28for,of,action%29.md)

Customize [`WebView`](./webview-swift.struct.md) display and interactions with view modifiers, such as:

- [`webViewBackForwardNavigationGestures(_:)`](../SwiftUI/view/webviewbackforwardnavigationgestures%28_%29.md)
- [`webViewMagnificationGestures(_:)`](../SwiftUI/view/webviewmagnificationgestures%28_%29.md)
- [`webViewLinkPreviews(_:)`](../SwiftUI/view/webviewlinkpreviews%28_%29.md)
- [`webViewTextSelection(_:)`](../SwiftUI/view/webviewtextselection%28_%29.md)
- [`webViewElementFullscreenBehavior(_:)`](../SwiftUI/view/webviewelementfullscreenbehavior%28_%29.md)
- [`webViewContextMenu(menu:)`](../SwiftUI/view/webviewcontextmenu%28menu%29.md)
- [`webViewContentBackground(_:)`](../SwiftUI/view/webviewcontentbackground%28_%29.md)

To further customize and control a web interaction, connect a [`WebView`](./webview-swift.struct.md) to a [`WebPage`](./webpage.md). The following example demonstrates this by configuring the view’s navigation title to be the webpage’s title, which the system updates automatically because [`WebPage`](./webpage.md) is an `Observable` type:

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

You can only bind a [`WebPage`](./webpage.md) to a single [`WebView`](./webview-swift.struct.md) at a time.

## Topics

### Creating web views
- [init(WebPage)](./webview-swift.struct/init%28_%29.md)
  Create a new WebView.
- [init(url: URL?)](./webview-swift.struct/init%28url%29.md)
  Create a new WebView with the specified URL.
### Modifying web interactions
- [WebView.BackForwardNavigationGesturesBehavior](./webview-swift.struct/backforwardnavigationgesturesbehavior.md)
  A type that defines the behavior of how horizontal swipe gestures trigger backward and forward page navigation.
- [WebView.LinkPreviewBehavior](./webview-swift.struct/linkpreviewbehavior.md)
  A type specifying the behavior for the presentation of link previews when pressing a link.
- [WebView.ActivatedElementInfo](./webview-swift.struct/activatedelementinfo.md)
  Contains information about an element the user activated in a webpage, which may be used to configure a context menu for that element.
- [WebView.ElementFullscreenBehavior](./webview-swift.struct/elementfullscreenbehavior.md)
  The behavior that determines whether a web view can display content full screen.
- [WebView.MagnificationGesturesBehavior](./webview-swift.struct/magnificationgesturesbehavior.md)
  The options for controlling the behavior for how magnification gestures interact with web views.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Essentials
- [Building a cross-platform web browser](./building-a-cross-platform-web-browser.md)
  Implement a browser on multiple platforms that loads content, manages navigation history, and saves favorite websites, using WebKit for SwiftUI.
- [class WebPage](./webpage.md)
  An object that controls and manages the behavior of interactive web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.struct)*