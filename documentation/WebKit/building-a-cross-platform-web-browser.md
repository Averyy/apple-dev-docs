# Building a cross-platform web browser

**Framework**: WebKit

Implement a browser on multiple platforms that loads content, manages navigation history, and saves favorite websites, using WebKit for SwiftUI.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+
- Xcode 26.4+

#### Overview

This sample project demonstrates how you can create a cross-platform web browser with SwiftUI and WebKit, in iOS 26 and later or macOS 26 and later. The sample displays web content in a [`WebView`](webview-swift.struct.md), and builds the following features:

- Load and observe web content with [`WebPage`](webpage.md).
- Display web content and enable browser behaviors using [`WebView`](webview-swift.struct.md).
- Observe and navigate browser history using [`WebPage.BackForwardList`](webpage/backforwardlist-swift.struct.md).
- Serve local HTML resources with a custom [`URLSchemeHandler`](urlschemehandler.md).
- Load website favicons asynchronously with [`LinkMetadata`](https://developer.apple.com/documentation/LinkPresentation/LinkMetadata).
- Export and share webpage content using [`WebPage`](webpage.md)’s [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) conformance.

The sample demonstrates how using these SwiftUI features to interact with web content simplifies your app compared to implementing them with [`WKWebView`](wkwebview.md) and related APIs.

> **Note**: This sample code project is associated with WWDC 2025 session 231: [`Meet WebKit for SwiftUI`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/231/).

#### Create an Observable Browser Model

The sample stores webpage and browser properties in an [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) class called `BrowserManager`, as shown below, enabling SwiftUI to automatically redraw views when properties change:

```swift
@Observable
class BrowserManager {
    let page: WebPage
    let privateBrowsingEnabled: Bool
    ...
}
```

The `BrowserManager` class initializes [`WebPage`](webpage.md) with a configuration that specifies a data store and registers custom URL scheme handlers. It also creates a `NavigationPolicyHandler` instance that implements [`WebPage.NavigationDeciding`](webpage/navigationdeciding.md) to intercept navigation requests and capture link-activated URLs, as shown here:

```swift
init(privateBrowsingEnabled: Bool = false) {
    self.privateBrowsingEnabled = privateBrowsingEnabled
    var configuration = WebPage.Configuration()

    // Use a nonpersistent data store for private browsing.
    configuration.websiteDataStore = privateBrowsingEnabled ? .nonPersistent() : .default()

    // Register a custom URL scheme handler for `local://` resources.
    if let localScheme = URLScheme("local") {
        configuration.urlSchemeHandlers[localScheme] = CustomSchemeHandler()
    }

    // Create the navigation handler and pass it to the `WebPage` as its navigation decider.
    let navigationHandler = NavigationPolicyHandler()
    self.page = WebPage(
        configuration: configuration,
        navigationDecider: navigationHandler
    )
    navigationHandler.onRequestIntercepted = { [weak self] value in
        self?.currentRequest = value.url
    }

    // Store the URL to open when someone initiates a link-activated navigation.
    navigationHandler.onOpenURL = { [weak self] url in
        self?.urlToOpen = url
    }
}
```

The sample’s `ContentView` creates a `BrowserManager` instance with the [`State`](https://developer.apple.com/documentation/SwiftUI/State) property wrapper and injects it into the view hierarchy using [`environment(_:)`](https://developer.apple.com/documentation/SwiftUI/View/environment(_:)). Subviews retrieve it with `@Environment(BrowserManager.self)`.

#### Load and Display Web Content

The sample uses [`WebPage`](webpage.md) because it’s an observable type that handles loading and tracks properties like the current URL and title. The sample keeps an instance of [`WebPage`](webpage.md) called `page` in `BrowserManager`, and specifies that `page` when it declares [`WebView`](webview-swift.struct.md), the SwiftUI view that renders it. The sample applies modifiers to enable common browser behaviors, as shown here:

```swift
WebView(browserManager.page)
    // Shows link previews when someone presses a link.
    .webViewLinkPreviews(.enabled)

    // Enables swipe gestures for navigation.
    .webViewBackForwardNavigationGestures(.enabled)

    // Makes web text content selectable.
    .webViewTextSelection(.enabled)

    // Enables system magnification gestures.
    .webViewMagnificationGestures(.enabled)

    // Makes web content fill the entire web view container.
    .webViewElementFullscreenBehavior(.enabled)

    // Links displaying the find-and-replace interface to the browser manager's
    // `findNavigatorIsPresented` property.
    .findNavigator(isPresented: $browserManager.findNavigatorIsPresented)
```

In macOS, the sample uses `webViewContextMenu` to provide a secondary-click menu with link-specific options.

#### Handle Navigation History

The `BrowserManager` class exposes navigation history as computed arrays from [`WebPage.BackForwardList`](webpage/backforwardlist-swift.struct.md), as the following code snippet demonstrates. The toolbar uses these arrays to populate back and forward buttons, where a tap navigates immediately and a long press reveals the full history.

```swift
// Webpage navigation history: back entries.
var backList: [WebPage.BackForwardList.Item] {
    page.backForwardList.backList
}

// Webpage navigation history: forward entries.
var forwardList: [WebPage.BackForwardList.Item] {
    page.backForwardList.forwardList
}
```

```swift
// Lists the back history as a menu.
Menu {
    ForEach(browserManager.backList.reversed()) { item in
        Button(item.title ?? item.url.absoluteString) {
            browserManager.navigateTo(item)
        }
    }
} label: {
    Label("Back", systemImage: "chevron.left")
} primaryAction: {
    // Navigates to the most recent back history item.
    if let last = browserManager.backList.last {
        browserManager.navigateTo(last)
    }
}
.disabled(browserManager.backList.isEmpty)
.menuIndicator(.hidden)
```

The view observes navigation events through [`navigations`](webpage/navigations.md), an async sequence that emits events as navigation progresses. If navigation throws an error, the view updates `isPresented` and stores the error information, like this:

```swift
// Listens for navigation events and presents an alert on error.
.task(id: browserManager.page.url) {
    if browserManager.page.url != nil {
        do {
            for try await event in browserManager.page.navigations {
                print(event)
            }
        } catch {
            self.isPresented = true
            self.error = error
        }
    }
}
```

When `isPresented` is `true`, the view presents an alert with the error’s localized description.

#### Load Local Html Files with a Custom Scheme

The sample registers `CustomSchemeHandler` for the `local` URL scheme. `CustomSchemeHandler` intercepts any navigation to a `local://` address and serves it from the app bundle instead of the network. The handler conforms to [`URLSchemeHandler`](urlschemehandler.md), locates the requested resource in the bundle, and yields the response and data, as follows:.

```swift
struct CustomSchemeHandler: URLSchemeHandler {
    func reply(for request: URLRequest) -> some AsyncSequence<URLSchemeTaskResult, any Error> {
        AsyncThrowingStream { continuation in
            guard let url = request.url else {
                continuation.finish(throwing: URLError(.badURL))
                return
            }

            guard url.scheme == "local" else {
                // Reject any nonlocal schemes.
                continuation.finish(throwing: URLError(.unsupportedURL))
                return
            }

            // Extract the last path component as the resource name.
            let resourceName = url.deletingPathExtension().lastPathComponent
            let resourceExtension = url.pathExtension.isEmpty ? "html" : url.pathExtension

            guard let resourceURL = Bundle.main.url(forResource: resourceName, withExtension: resourceExtension),
                  let data = try? Data(contentsOf: resourceURL) else {
                continuation.finish(throwing: URLError(.fileDoesNotExist))
                return
            }

            let response = URLResponse(
                url: url,
                mimeType: mimeTypeForExtension(resourceExtension),
                expectedContentLength: data.count,
                textEncodingName: "utf-8"
            )

            continuation.yield(.response(response))
            continuation.yield(.data(data))
            continuation.finish()
        }
    }
}
```

#### Display Website Favicons

The favorite row views that the sample declares in `FavoriteRowView` load each website’s favicon asynchronously using [`LinkMetadata`](https://developer.apple.com/documentation/LinkPresentation/LinkMetadata) from the [`Link Presentation`](https://developer.apple.com/documentation/LinkPresentation) framework, as shown in the code below. The fetch runs in a [`task(id:name:executorPreference:priority:file:line:_:)`](https://developer.apple.com/documentation/SwiftUI/View/task(id:name:executorPreference:priority:file:line:_:)) modifier keyed to the favorite’s URL, so it restarts automatically whenever the URL changes.

```swift
.task(id: webpage.url) {
    // Asynchronously load the favicon.
    favicon = await fetchFavicon(for: webpage.url)
}
```

The `fetchFavicon(for:)` method initializes a [`LinkMetadata`](https://developer.apple.com/documentation/LinkPresentation/LinkMetadata) value by fetching the URL, then extracts the icon as [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) using the `.icon` attachment, as the code below demonstrates. Using [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) supports all common favicon formats — including ICO, PNG, and JPEG — directly.

```swift
private func fetchFavicon(for url: URL) async -> Image? {
    guard let metadata = try? await LinkMetadata(fetching: url, timeout: .seconds(30)),
          let image = try? await metadata.media(.icon, as: Image.self) else {
        return nil
    }

    return image
}
```

While the favicon loads, the row displays a placeholder globe icon.

#### Export and Share Webpage Content

The [`WebPage`](webpage.md) type conforms to [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable), so it works directly with [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) and the file exporter. The sample places both options in a toolbar menu, like this:

```swift
Menu {
    // Create the share sheet menu item.
    ShareLink(item: browserManager.page, preview: SharePreview(browserManager.page.title))

    // Create a menu item that copies the URL to the clipboard.
    if let url = browserManager.page.url {
        Button {
            browserManager.copyToPasteboard(url)
        } label: {
            Label("Copy Address", systemImage: "doc.on.doc")
        }
    }

    // Create the export menu.
    Menu {
        ForEach(WebPage.exportedContentTypes(), id: \.self) { type in
            Button("Save as \(type.localizedDescription ?? type.description)") {
                contentTypes = [type]
                showFileExporter = true
            }
        }
    } label: {
        Label("Export", systemImage: "square.and.arrow.up")
    }
}
```

The [`exportedContentTypes(visibility:)`](https://developer.apple.com/documentation/CoreTransferable/Transferable/exportedContentTypes(visibility:)) method returns the file formats the current page supports, so the export menu always reflects what the page can produce.

## See Also

- [struct WebView](webview-swift.struct.md)
  A view that displays some web content.
- [class WebPage](webpage.md)
  An object that controls and manages the behavior of interactive web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/building-a-cross-platform-web-browser)*