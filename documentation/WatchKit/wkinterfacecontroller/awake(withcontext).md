# awake(withContext:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Initializes the interface controller with the specified context data.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func awake(withContext context: Any?)
```

```objc
- (void) awakeWithContext:(id) context;
```

## Mentions

- [Navigating Between Scenes](../navigating-between-scenes.md)
- [Working with the watchOS app life cycle](../working-with-the-watchos-app-life-cycle.md)

#### Discussion

The system calls this method at initialization time to provide the interface controller with any relevant contextual data from a previous interface controller. Use this method to finish the initialization of your interface. For example, you might use this method to load data and to set the values for labels, images, tables, and other interface objects in your storyboard scene. If context data is available, use it to assist in the configuration of the new interface controller.

The default implementation of this method does nothing.

## Parameters

- `context`: The context object (if any) provided by the previous interface controller. This parameter may be `nil`. If it is not `nil`, you are responsible for saving a reference to the provided object and using it to configure your interface controller.

## See Also

### Creating the interface controller
- [init()](./init%28%29.md)
  Returns an initialized interface controller object.
- [func setTitle(String?)](./settitle%28_%29.md)
  Sets the title of the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:))*