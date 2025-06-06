# makeTouchBar()

**Framework**: UIKit  
**Kind**: method

Asks the receiving responder to create and configure a Touch Bar object.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
func makeTouchBar() -> NSTouchBar?
```

#### Return Value

A newly created Touch Bar object.

#### Discussion

Override this method in a responder, such as [`UIViewController`](uiviewcontroller.md), to create and configure a Touch Bar object for the responder.

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

- [var touchBar: NSTouchBar?](uiresponder/touchbar.md)
  The Touch Bar object for the responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/maketouchbar())*