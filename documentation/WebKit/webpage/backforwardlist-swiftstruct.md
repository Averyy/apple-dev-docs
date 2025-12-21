# WebPage.BackForwardList

**Framework**: WebKit  
**Kind**: struct

An observable representation of a webpage’s previously loaded resources.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
struct BackForwardList
```

#### Overview

This type can be used to facilitate navigating to prior or subsequent loaded resources and for observing when new entries get added or removed.

In this example, the back-forward list is used to create a SwiftUI View to facilitate navigating to previous or next items:

```swift
private struct BackForwardMenuView: View {
    struct LabelConfiguration {
        let text: String
        let systemImage: String
    }

    let list: [WebPage.BackForwardList.Item]
    let label: LabelConfiguration
    let navigateToItem: (WebPage.BackForwardList.Item) -> Void

    var body: some View {
        Menu {
            ForEach(list) { item in
                Button(item.title ?? item.url.absoluteString) {
                    navigateToItem(item)
                }
            }
        } label: {
            Label(label.text, systemImage: label.systemImage)
                .labelStyle(.iconOnly)
        } primaryAction: {
            navigateToItem(list.first!)
        }
        .disabled(list.isEmpty)
    }
}
```

The view can then be used for both the back and forward list using a specific [`WebPage`](webpage.md):

```swift
struct ContentView: some View {
    @State private var page = WebPage()

    var body: some View {
        WebView(page)
            .toolbar {
                ToolbarItemGroup {
                    ToolbarBackForwardMenuView(
                        list: page.backForwardList.backList.reversed(),
                        label: .init(text: "Backward", systemImage: "chevron.backward")
                    ) {
                        viewModel.page.load($0)
                    }

                    ToolbarBackForwardMenuView(
                        list: page.backForwardList.forwardList,
                        label: .init(text: "Forward", systemImage: "chevron.forward")
                    ) {
                        viewModel.page.load($0)
                    }
                }
            }
    }
}
```

Because [`backForwardList`](webpage/backforwardlist-swift.property.md) is an observable property, the states of these buttons are automatically updated.

## Topics

### Structures
- [WebPage.BackForwardList.Item](webpage/backforwardlist-swift.struct/item.md)
  A representation of a resource that a webpage previously visited.
### Instance Properties
- [var backList: [WebPage.BackForwardList.Item]](webpage/backforwardlist-swift.struct/backlist.md)
  The array of items that precede the current item.
- [var currentItem: WebPage.BackForwardList.Item?](webpage/backforwardlist-swift.struct/currentitem.md)
  The current item.
- [var forwardList: [WebPage.BackForwardList.Item]](webpage/backforwardlist-swift.struct/forwardlist.md)
  The array of items that follow the current item.
### Subscripts
- [subscript(Int) -> WebPage.BackForwardList.Item?](webpage/backforwardlist-swift.struct/subscript(_:).md)
  Accesses the item at the relative offset from the current item.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WebPage.NavigationEvent](webpage/navigationevent.md)
  A particular state that occurs during the progression of a navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/backforwardlist-swift.struct)*