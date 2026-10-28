# presentController(withNames:contexts:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Presents a page-based interface modally.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func presentController(withNames names: [String], contexts: [Any]?)
```

```objc
- (void) presentControllerWithNames:(NSArray<NSString *> *) names contexts:(NSArray *) contexts;
```

## Mentions

- [Navigating Between Scenes](../navigating-between-scenes.md)

## Discussion

After calling this method, WatchKit loads and initializes the new interface controllers and animates them into position on top of the current interface controller. A modal interface slides up from the bottom of the screen and completely cover the previous interface. WatchKit displays the first interface controller in the `names` array initially. The user can navigate to the other interfaces by swiping horizontally.

The title of the modal interface is set to the string `Cancel` by default. Change the title using the [`setTitle(_:)`](./settitle%28_%29.md) method. Tapping the title dismisses the interface automatically. To dismiss the interface programmatically, call the [`dismiss()`](./dismiss%28%29.md) method.

Always call this method from your WatchKit extension’s main thread.

## Parameters

- `names`: An array of strings, each of which contains the name of an interface controller you want to display in the page-based interface. In your storyboard, the name of an interface controller is stored in the object’s Identifier property, which is located in the attributes inspector. The order of the strings in the array is used to set the order of the corresponding interface controllers. This parameter must not be `nil` or an empty array.
- `contexts`: An array of context objects to pass to the new interface controllers. Use the objects in this array to communicate important information to the new interface controllers, such as the data to display or any relevant state information. You may specify `nil` for this parameter, but doing so is not recommended.

  Each object in the array is passed to the interface controller at the same index in the `names` parameter.

## See Also

### Presenting interface controllers modally
- [func presentController(withName: String, context: Any?)](./presentcontroller%28withname,context%29.md)
  Presents a single interface controller modally.
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](./presentcontroller%28withnamesandcontexts%29.md)
  Presents a page-based interface modally.
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](./presentalert%28withtitle,message,preferredstyle,actions%29.md)
  Presents an alert or action sheet over the current interface controller.
- [enum WKAlertControllerStyle](../wkalertcontrollerstyle.md)
  Constants indicating the styles for standard system alerts.
- [func dismiss()](./dismiss%28%29.md)
  Dismisses the current interface controller from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withnames:contexts:))*