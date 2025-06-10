# Creating an intuitive and effective UI in watchOS 10

**Framework**: watchOS apps

Provide an even more streamlined, consistent, and glanceable user experience with new design features.

#### Overview

watchOS 10 provides a redesigned user interface that focuses on relevant, glanceable content and consistent navigation, and takes advantage of the high-quality display with full-screen color and images.

When designing your app, use these features to create efficient, intuitive navigation:

- [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView) provides a set of views that people can scroll through using the Digital Crown.
- [`NavigationSplitView`](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView) toggles between a source list and a set of detail views.
- [`NavigationStack`](https://developer.apple.com/documentation/SwiftUI/NavigationStack) moves into and back out of a hierarchy of views.

Use these features to make your app consistent and visually coherent:

- [`Toolbars`](https://developer.apple.com/documentation/SwiftUI/Toolbars) guarantee consistent size and placement for buttons.
- [`matchedGeometryEffect(id:in:properties:anchor:isSource:)`](https://developer.apple.com/documentation/SwiftUI/View/matchedGeometryEffect(id:in:properties:anchor:isSource:)) animates changes to persistent elements across different tabs.
- [`Color`](https://developer.apple.com/documentation/SwiftUI/Color) provides opportunities for branding, glanceable information, and additional context.
- [`Material`](https://developer.apple.com/documentation/SwiftUI/Material) help create consistency, a clear hierarchy, and a sense of place.

For design guidance, see Human Interface Guidelines > [`Designing for watchOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-watchos).

#### Scroll Through Views Using the Digital Crown

The Digital Crown provides a precise input device that people can use to navigate between apps, scroll through an app’s content, and make precise selections without obscuring the display. To get the most out of the Digital Crown, emphasize vertical scrolling over horizontal scrolling in your app and use system controls that already support the Digital Crown, like the [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker). In addition, watchOS 10 adds the ability to scroll vertically through a set of pages.

To create vertical pagination, use a [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView) and set the [`tabViewStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/tabViewStyle(_:)) to [`verticalPage`](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/verticalPage).

```swift
@Binding var selected: Item

var body: some View {
    TabView(selection: $selected) {
        ForEach(Item.allCases) { item in
            // Create a view for the item.
            Text("\(item.title) tab")
        }
    }
    .tabViewStyle(.verticalPage)
}
```

The system displays the selected tab and places a page indicator next to the Digital Crown. People can scroll vertically through the pages with their finger, or using the Digital Crown.

![A screenshot of an Apple Watch with a tab view with the third tab selected. The page indicator shows six dots next to the Digital Crown. The dot for the selected tab is highlighted.](https://docs-assets.developer.apple.com/published/d09c27b6757df65a7ae5f5d936c8c781/scrolling-through-vertical-tabs%402x.png)

Use a [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView) to display a set of distinct, purposeful views. Give each view a clear purpose, and consider limiting the view’s content to a single screen’s worth of information. However, the system does support longer views, transitioning seamlessly from scrolling between views, and scrolling through a longer view’s content. If you have longer views, consider placing them after your app’s fixed-height views.

```swift
@Binding var selected: Item
var body: some View {
    TabView(selection: $selected) {
        ForEach(Item.allCases) { item in
            // Create a screen-sized view for each item.
            Text("\(item.title) tab")
        }
        
        // End with a longer view.
        ScrollView {
            Text("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n")
        }
    }
    .tabViewStyle(.verticalPage)
}
```

When scrolling through a longer view’s content, the system expands the selected dot in the page control to show the scroll position within the longer view.

![A screenshot of an Apple Watch showing a tab view with the final, longer view selected. The selected dot in the page indicator has expanded to show the scroll position in the long view.](https://docs-assets.developer.apple.com/published/846d4b3392e97185c673ca0e5393f0af/scrolling-in-longer-views%402x.png)

For additional design guidance, see Human Interface Guidelines > [`Digital Crown`](https://developer.apple.com/design/Human-Interface-Guidelines/digital-crown) and [`Page controls`](https://developer.apple.com/design/Human-Interface-Guidelines/page-controls).

#### Toggle Between a Source List and Detail Views

In macOS, iOS, and iPadOS, split views are used to present two or more columns of data. In watchOS 10, a [`NavigationSplitView`](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView) is the ideal way to display a source list and the corresponding detail views. If the context is large enough to show multiple columns, the system displays a list of items in the leading column. People can then choose one or more items in a leading column to display details about those items in subsequent columns.

Similar to the experience on an iPhone in portrait orientation, the `NavigationSplitView` in watchOS 10 only shows one column at a time. For example, your app may display a [`List`](https://developer.apple.com/documentation/SwiftUI/List) in the source view. When someone selects an item from the list, the `NavigationSplitView` automatically animates to the corresponding detail view. When the person taps the list icon, the system returns to the source view. The system automatically handles animating the transition between source and detail view.

To create a split view, instantiate a `NavigationSplitView` instance. Pass a `List` as the source view, and create a detail view based on the selection.

```swift
@Binding var selected: Item?

var body: some View {
    NavigationSplitView() {

        List(selection: $selected) {
            ForEach(Item.allCases, id: \.self) { item in
                NavigationLink(item.rawValue.uppercased(),
                               value: item)
            }
        }
        .listStyle(.carousel)
    } detail: {
        DetailView(selected: $selected)
    }

}
```

You can also combine the split view with a vertical tab view, letting people scroll through the detail views.

```swift
@Binding var selected: Item?

var body: some View {
    NavigationSplitView() {

        List(selection: $selected) {
            ForEach(Item.allCases, id: \.self) { item in
                NavigationLink(item.rawValue.uppercased(),
                               value: item)
            }
        }
        .containerBackground(.green.gradient,
                             for: .navigation)
        .listStyle(.carousel)
    } detail: {
        TabView(selection: $selected) {
        ForEach(Item.allCases, id: \.self) { item in
            ItemView(item: item)
                .tag(Optional(item))
                .containerBackground(.blue.gradient,
                                     for: .tabView)
        }
    }
    .tabViewStyle(.verticalPage)}
}
```

> ❗ **Important**: While the code for the `List` and the `TabView` look very similar, there is a significant difference. The `List` expects an [`Optional`](https://developer.apple.com/documentation/Swift/Optional) for the `selected` value. If `selected` is `nil`, that means nothing is selected. If it’s not `nil`, the system unwraps its value and compares the value to the `id` for each item in the list. On the other hand, the `TabView` doesn’t unwrap the `selected` value. It just compares `selected` to the tab item’s [`tag(_:includeOptional:)`](https://developer.apple.com/documentation/SwiftUI/View/tag(_:includeOptional:)). As a result, you either need to unwrap `selected` before passing it to the tab view, or you need to wrap the tag values in an `Optional` before passing them to the `tag(_:)` modifier.

When using a split view in watchOS, consider the following best practices:

- Automatically open the split view to its most relevant detail view. You can use location, recency, frequency, or some other indication of user intent to determine the detail view to display.
- There’s no need to add a title to the source list, or a cancel button or navigation controls to the detail view. Avoiding extraneous labels results in a shorter navigation bar, giving you more room to display data.
- Consider making your detail views unmistakeable at a glance, so they also don’t need a title.
- You can use the source list to present comparative data. For example, a weather app might display the temperature at each location, or a world clock might display the time in each city.

For additional design guidance, see Human Interface Guidelines > [`Split views`](https://developer.apple.com/design/Human-Interface-Guidelines/split-views).

#### Move Through a Hierarchy of Views

While the `TabView` and `NavigationSplitView` provide new navigation paradigms, they aren’t your only option. If your app doesn’t pivot between a detail view and a source list, or if it needs more than a few vertically paginated tabs, consider using a [`NavigationStack`](https://developer.apple.com/documentation/SwiftUI/NavigationStack). While the `NavigationStack` isn’t a new feature, it is still an effective way to navigate an arbitrary hierarchy of views.

To create a `NavigationStack`:

1. Create an array to store the stack.
2. Pass a [`Binding`](https://developer.apple.com/documentation/SwiftUI/Binding) to the array as the `path` to the `NavigationStack` constructor.
3. Use the [`navigationDestination(for:destination:)`](https://developer.apple.com/documentation/SwiftUI/View/navigationDestination(for:destination:)) modifier to provide the view for the current data from the front of the array.

Your app can then modify the array directly, or use [`NavigationLink`](https://developer.apple.com/documentation/SwiftUI/NavigationLink) instances. These links push a value onto the array when someone taps it.

```swift
@State var stack = [Int]()

var body: some View {
    NavigationStack(path: $stack) {
        // Create the root view.
        Text("Main page")
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    NavigationLink(value: 2) {
                        Image(systemName: "chevron.right")
                    }
                }
            }
            // Create a view for the top value in the stack.
            .navigationDestination(for: Int.self) { value in
                Text("Second page")
            }
    }
}
```

When creating a navigation stack in watchOS, consider the following best practices:

- To streamline navigation, keep the view hierarchy as shallow as possible.
- Use a large title on the root view.
- Don’t use a title on any subsequent views where a back button is present.

#### Place Buttons Consistently with the Toolbar

If your app uses a `NavigationSplitView` or `NavigationStack`, you can place buttons in a [`toolbar(content:)`](https://developer.apple.com/documentation/SwiftUI/View/toolbar(content:)) and provide a consistent size, location, and appearance for the buttons. If the view has scrolling content, the buttons remain visible above the content.

You can place both a leading and trailing button in the top toolbar. The system automatically moves the page’s navigation title and the time to make space for these buttons. Additionally, you can place up to three buttons in the bottom toolbar. If you have three buttons in the bottom bar, you can make the center button more prominent by making it larger.

```swift
var body: some View {
    NavigationStack {
        Text("Main View")
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button {
                        // Perform an action here.
                    } label: {
                        Image(systemName:"suit.heart")
                    }
                }
                ToolbarItem(placement: .topBarTrailing) {
                    Button {
                        // Perform an action here.
                    } label: {
                        Image(systemName:"suit.club")
                    }
                }
                ToolbarItemGroup(placement: .bottomBar) {
                    Button {
                        // Perform an action here.
                    } label: {
                        Image(systemName:"suit.diamond")
                    }
                    
                    Button {
                        // Perform an action here.
                    } label: {
                        Image(systemName:"star")
                    }
                    .controlSize(.large)
                    .background(.red, in: Capsule())
                    
                    Button {
                        // Perform an action here.
                    } label: {
                        Image(systemName:"suit.spade")
                    }
                }
            }
    }
}
```

![A screenshot of an Apple Watch showing the root view of a navigation stack. The view has a heart button in the top leading position, a club button in the top trailing, a diamond in the bottom leading and a spade in the bottom trailing. It also has a larger, red star button in the center of the bottom toolbar.](https://docs-assets.developer.apple.com/published/9246721d7cffae645cc6f8a200e0eeec/tab-bar-buttons%402x.png)

You can also place a button in the scrolling view by using the [`primaryAction`](https://developer.apple.com/documentation/SwiftUI/ToolbarItemPlacement/primaryAction) placement. By default, a scrolling toolbar button remains hidden until people reveal it by scrolling up. People frequently scroll to the top of a scrolling view, so discovering a toolbar button is automatic.

- Use toolbar buttons to offer important functionality that’s related to the view, but not necessarily part of the view’s main purpose. A primary action might work better as a button in the view itself.
- By default, the system automatically displays the list icon or back button in the leading top toolbar position. As a result, you often only place your own button in the top trailing position.

For additional design guidance, see Human Interface Guidelines > [`Toolbars`](https://developer.apple.com/design/Human-Interface-Guidelines/toolbars).

#### Provide Continuity with Persistent Elements

You can display the same element on multiple pages to create a sense of continuity between the pages. For example, when working with vertical tab views, use the [`matchedGeometryEffect(id:in:properties:anchor:isSource:)`](https://developer.apple.com/documentation/SwiftUI/View/matchedGeometryEffect(id:in:properties:anchor:isSource:)) modifier to animate changes to an element’s size and position between tabs.

For example, the following screenshot shows a books icon in the middle of the first page.

![ A screenshot of an Apple Watch showing the first page of a vertical tab view, with the books icon in the middle of the page.](https://docs-assets.developer.apple.com/published/9daa407c28fad117b715a57ac5d4f8e9/persistent-icon-page-1%402x.png)

Then, when someone uses the digital crown to scroll to the next page, the icon shrinks and moves into the toolbar.

![ A screenshot of an Apple Watch showing the second page of a vertical tab view, with the books icon moved to the upper right edge of the toolbar.](https://docs-assets.developer.apple.com/published/5513cca02df225c630c5987d2780c507/persistent-icon-page-2%402x.png)

The following code uses the `matchedGeometryEffect` modifier to create that effect.

```swift
NavigationStack {
    TabView(selection: $pageNumber) {

        VStack {
            Image(systemName: "books.vertical.fill")
                .imageScale(.large)
                .matchedGeometryEffect(
                    id: bookIcon,
                    in: library,
                    properties:  .frame,
                    isSource: pageNumber == 0)
            Text("Books")
        }
        .tag(0)

        VStack {
            BookList()
        }
        .tag(1)
    }
    .tabViewStyle(.verticalPage)
    .toolbar {
        ToolbarItem(placement: .topBarLeading) {
            Image(systemName: "books.vertical.fill")

                .matchedGeometryEffect(
                    id: bookIcon,
                    in: library,
                    properties:  .frame,
                    isSource: pageNumber != 0)
        }
    }
}
```

In this example, the icon appears in the first tab’s view and in the toolbar. The `isSource` parameter determines which version gets rendered. If `pageNumber` is `0`, someone is viewing the first page, so the system renders the version inside the tab view. If `pageNumber` is set to a different value, the system renders the version in the toolbar. When `pageNumber` changes, the system animates the changes to the icon’s frame, matching the animation to the Digital Crown.

#### Provide Additional Information with Color Backgrounds

You can use full color backgrounds to convey information about your app.

Consider colors that:

- Relate to your app’s branding.
- Evoke a particular emotion, such as the calming blue background in Sleep.
- Convey a sense of space. For example, Fitness has a black background on the main screen, but uses red, green, and blue background colors for the Move, Exercise, and Stand views.
- Display information at a glance. For example, World Clock uses solar gradients to show the time of day.
- Indicate a state change. Timer also uses a black background, but changes to bright orange when the timer is done.

Normal views can just set the [`background(alignment:content:)`](https://developer.apple.com/documentation/SwiftUI/View/background(alignment:content:)) to the desired color. However, for anything presented by a `NavigationSplitView`, `NavigationStack`, or `TabView`, use the [`containerBackground(_:for:)`](https://developer.apple.com/documentation/SwiftUI/View/containerBackground(_:for:)) modifier instead and pass in either the [`navigation`](https://developer.apple.com/documentation/SwiftUI/ContainerBackgroundPlacement/navigation) or [`tabView`](https://developer.apple.com/documentation/SwiftUI/ContainerBackgroundPlacement/tabView) value for the placement. The `containerBackground` modifier also supports displaying a gradient using the [`gradient`](https://developer.apple.com/documentation/SwiftUI/Color/gradient) modifier.

For example, the following code adds a green gradient to the split view’s source list.

```swift
@Binding var selected: Item?

var body: some View {
    NavigationSplitView() {

        List(selection: $selected) {
            ForEach(Item.allCases, id: \.self) { item in
                NavigationLink(item.rawValue.uppercased(),
                               value: item)
            }
        }
        .containerBackground(.green.gradient,
                             for: .navigation)
        .listStyle(.carousel)
    } detail: {
        DetailView(selected: $selected)
    }

}
```

This example adds a blue gradient to a tab item.

```swift
@Binding var selected: Item?

var body: some View {
    TabView(selection: $selected) {
        ForEach(Item.allCases) { item in
            Text("\(item.title) tab")
                .tag(Optional(item))
                .containerBackground(.blue.gradient,
                                     for: .tabView)
        }
    }
    .tabViewStyle(.verticalPage)
}
```

For additional design guidance, see Human Interface Guidelines > [`Color`](https://developer.apple.com/design/Human-Interface-Guidelines/color).

#### Indicate Hierarchy and Context with Materials

Use [`Material`](https://developer.apple.com/documentation/SwiftUI/Material) effects to improve legibility, define an information hierarchy, and provide context.

For example, the system automatically adds the following:

- A vibrant fill `material` to controls like buttons and list cells.
- A full-screen, thin `material` to presented views, like sheets and full-screen covers. This effect lets the color of the covered view show through, helping orient the wearer within the app.
- A blur effect behind the navigation bar.

Additionally, the system provides vibrant text labels in [`primary`](https://developer.apple.com/documentation/SwiftUI/ShapeStyle/primary), [`secondary`](https://developer.apple.com/documentation/SwiftUI/ShapeStyle/secondary-swift.property), [`tertiary`](https://developer.apple.com/documentation/SwiftUI/ShapeStyle/tertiary-swift.property), and [`quaternary`](https://developer.apple.com/documentation/SwiftUI/ShapeStyle/quaternary-swift.property)  prominence levels for creating a typographic hierarchy. You can also add vibrant versions of all the system colors to ensure legibility over full-color backgrounds.

For example, use the [`foregroundStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/foregroundStyle(_:)) to set a hierarchical text style. Or use a [`borderedProminent`](https://developer.apple.com/documentation/SwiftUI/PrimitiveButtonStyle/borderedProminent) button style to make a button more prominent.

```swift
@State var item: Item

var body: some View {
    VStack {
        HStack {
            Text(item.title)
                .font(.headline)
                .foregroundStyle(.primary)
            Spacer()
        }
        .scenePadding(.horizontal)
        
        HStack {
            Text(item.subtitle)
                .font(.subheadline)
                .foregroundStyle(.secondary)
            Spacer()
        }
        .scenePadding(.horizontal)
        
        Spacer()
        
        Text(item.bodyText)
            .foregroundStyle(.tertiary)
            .scenePadding(.horizontal)
        
        Spacer()
        
        Button {
            // Perform an action here.
        } label: {
            Text("Action")
        }
        .buttonStyle(.borderedProminent)
    }
```

![A screenshot of an Apple Watch showing a sheet displayed over a view with the green gradient showing through. The sheet contains a title, subtitle, body text, and a button. Each Text view uses one of the hierarchical materials to set its foreground color. The button uses the borderedProminant style to set it's background color.](https://docs-assets.developer.apple.com/published/8087a8a273dde1f4483543c9f56f7406/setting-hierarchy-with-materials%402x.png)

For additional design guidance, see Human Interface Guidelines > [`Materials`](https://developer.apple.com/design/Human-Interface-Guidelines/materials).

## See Also

- [Updating your app and widgets for watchOS 10](updating-your-app-and-widgets-for-watchos-10.md)
  Integrate SwiftUI elements and watch-specific features, and build widgets for the Smart Stack.
- [Building a watchOS app](building_a_watchos_app.md)
  Set up your app’s life cycle and create its user interface with SwiftUI.
- [watchOS updates](../Updates/watchos.md)
  Learn about important changes to watchOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/creating-an-intuitive-and-effective-ui-in-watchos-10)*