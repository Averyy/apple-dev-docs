# XCUIElementQuery

**Framework**: XCUIAutomation  
**Kind**: class  
**Role**: Class

An object that defines the search criteria a test uses to identify UI elements.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
@MainActor
class XCUIElementQuery
```

```objc
@interface XCUIElementQuery : NSObject
```

## Mentions

- [Recording UI automation for testing](./recording-ui-automation-for-testing.md)

## Discussion

Use element queries to find UI elements in your app that you interact with in the tests, to test for the presence of expected elements, or to discover elements to test their values.

For example, this test uses an element query to find the “Add Book” button, and after clicking the button, checks that there’s one button in an outline view cell titled “Untitled Book”. If the test can’t find the “Add Book” button, or there isn’t one “Untitled Book” cell, then the test fails.

```swift
@MainActor
func testClickingAddCreatesAnUntitledBook() throws {
    let app = XCUIApplication()
    app.launch()
    let list = app.windows["Reading Journal"]
    list.toolbars.children(matching: .button)["Add Book"].click()
    XCTAssertEqual(list.outlines["Sidebar"].cells.containing(.button, identifier:"Untitled Book").count, 1)
}
```

## Topics

### Creating new queries
- [func children(matching: XCUIElement.ElementType) -> XCUIElementQuery](./xcuielementquery/children%28matching%29.md)
  Returns a new query that matches all direct children of the requested type.
- [func descendants(matching: XCUIElement.ElementType) -> XCUIElementQuery](./xcuielementquery/descendants%28matching%29.md)
  Returns a new query that matches all descendants of the requested type.
- [func containing(NSPredicate) -> XCUIElementQuery](./xcuielementquery/containing%28_%29.md)
  Returns a new query that matches elements containing a descendant that meets the logical conditions of the provided predicate.
- [func containing(XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery](./xcuielementquery/containing%28_,identifier%29.md)
  Returns a new query that matches elements that contain a descendant of the requested type and an identifying property that matches a provided identifier.
- [func matching(identifier: String) -> XCUIElementQuery](./xcuielementquery/matching%28identifier%29.md)
  Returns a new query that matches elements that have an identifying property that matches a provided identifier.
- [func matching(NSPredicate) -> XCUIElementQuery](./xcuielementquery/matching%28_%29.md)
  Returns a new query that matches elements that meet the logical conditions of the provided predicate.
- [func matching(XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery](./xcuielementquery/matching%28_,identifier%29.md)
  Returns a new query that matches elements of the requested type and have an identifying property that matches a provided identifier.
### Accessing matched elements
- [var allElementsBoundByAccessibilityElement: [XCUIElement]](./xcuielementquery/allelementsboundbyaccessibilityelement.md)
  Immediately evaluates the query and returns an array of elements bound to the resulting accessibility elements.
- [var allElementsBoundByIndex: [XCUIElement]](./xcuielementquery/allelementsboundbyindex.md)
  Immediately evaluates the query and returns an array of elements bound by the index of each result.
- [var count: Int](./xcuielementquery/count.md)
  Evaluates the query and returns the number of elements that match.
- [var element: XCUIElement](./xcuielementquery/element.md)
  The query’s single matching element.
- [func element(boundBy: Int) -> XCUIElement](./xcuielementquery/element%28boundby%29.md)
  Uses an index into the query’s results to determine which underlying accessibility element to use.
- [func element(matching: NSPredicate) -> XCUIElement](./xcuielementquery/element%28matching%29.md)
  Matches the predicate.
- [func element(matching: XCUIElement.ElementType, identifier: String?) -> XCUIElement](./xcuielementquery/element%28matching,identifier%29.md)
  Matches the provided element type and identifier.
- [subscript(String) -> XCUIElement](./xcuielementquery/subscript%28_%29.md)
  Returns a descendant element that matches a provided identifier.
- [func element(at: Int) -> XCUIElement](./xcuielementquery/element%28at%29.md)
  Returns an element that resolves to the index into the query’s result set.
### Debugging element queries
- [var debugDescription: String](./xcuielementquery/debugdescription.md)
  Provides debugging information about the query.
### Identifying window buttons
- [let XCUIIdentifierCloseWindow: String](./xcuiidentifierclosewindow.md)
  The identifier for a window’s close button.
- [let XCUIIdentifierFullScreenWindow: String](./xcuiidentifierfullscreenwindow.md)
  The identifier for a window’s full-screen button.
- [let XCUIIdentifierMinimizeWindow: String](./xcuiidentifierminimizewindow.md)
  The identifier for a window’s minimize button.
- [let XCUIIdentifierZoomWindow: String](./xcuiidentifierzoomwindow.md)
  The identifier for a window’s zoom button.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [XCUIElementTypeQueryProvider](./xcuielementtypequeryprovider.md)

## See Also

### UI element queries
- [protocol XCUIElementTypeQueryProvider](./xcuielementtypequeryprovider.md)
  A type that provides ready-made queries for locating descendant UI elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery)*