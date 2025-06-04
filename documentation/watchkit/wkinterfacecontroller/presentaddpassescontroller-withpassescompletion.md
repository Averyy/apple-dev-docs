# presentAddPassesController(withPasses:completion:)

**Framework**: WatchKit  
**Kind**: method

Displays a modal interface for presenting passes to the user.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func presentAddPassesController(withPasses passes: [PKPass]) async
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))

#### Discussion

Use this method to display PassKit passes to the user and to give the user the option to add them to their pass library. This method executes asynchronously, returning shortly after you call it. During a subsequent run loop cycle, the system displays the pass interface over the current interface controller. Always call this method from your WatchKit extension’s main thread.

The user dismisses the interface using the built-in controls. At dismissal time, the interface controller executes your `completion` block so that you can perform any relevant cleanup tasks.

## Parameters

- `passes`: An array of   objects that you want to present to the user.
- `completion`: The block to execute when the user is ready to dismiss the interface. Use this block to perform any cleanup tasks related to the dismissal of the modal interface. This block has no return value and takes no parameters.

## See Also

- [func dismissAddPassesController()](dismissaddpassescontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaddpassescontroller()))
  Dismisses the pass interface controller


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaddpassescontroller(withpasses:completion:))*