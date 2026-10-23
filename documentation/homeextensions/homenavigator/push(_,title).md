# push(_:title:)

**Framework**: HomeExtensions  
**Kind**: method  
**Role**: Instance Method

Pushes a page onto the Home app’s navigation stack.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
final func push(_ value: some Hashable, title: String? = nil)
```

#### Discussion

To provide the page’s view, add a matching `homeEmbeddedNavigationDestination(for:destination:)` modifier to your root view. The Home app manages back navigation.

For example:

```swift
context.navigator.push(Route.schedule, title: "Schedule")
```

## Parameters

- `value`: A value that identifies the page being pushed.
- `title`: The title to display in the navigation bar.  Pass `nil` to leave the title blank.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homenavigator/push(_:title:))*