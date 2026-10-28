# makeTouchBar()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the receiving responder to create and configure a Touch Bar object.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
func makeTouchBar() -> NSTouchBar?
```

```objc
- (NSTouchBar *) makeTouchBar;
```

## Return Value

A newly created Touch Bar object.

## Discussion

Override this method in a responder, such as [`UIViewController`](../uiviewcontroller.md), to create and configure a Touch Bar object for the responder.

```swift
#if targetEnvironment(macCatalyst)
extension RecipeDetailViewController: NSTouchBarDelegate {
    override func makeTouchBar() -> NSTouchBar? {
        let touchBar = NSTouchBar()
        touchBar.delegate = self
    
        touchBar.defaultItemIdentifiers = [
            .flexibleSpace,
            .deleteRecipe,
            .flexibleSpace,
            .editRecipe,
            .toggleRecipeIsFavorite,
            .flexibleSpace
        ]
    
        return touchBar
    }

    func touchBar(_ touchBar: NSTouchBar, makeItemForIdentifier identifier: NSTouchBarItem.Identifier) -> NSTouchBarItem? {
        let touchBarItem: NSTouchBarItem?
        // ...
        return touchBarItem
    }

#endif
```

## See Also

### Managing the Touch Bar
- [var touchBar: NSTouchBar?](./touchbar.md)
  The Touch Bar object for the responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/maketouchbar())*