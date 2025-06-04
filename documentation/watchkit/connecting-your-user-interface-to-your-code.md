# Connecting Your User Interface to Your Code

**Framework**: Watchkit

Connect the interface objects in your storyboard to outlets and action methods in your WatchKit extension.

## Overview

The code in your WatchKit extension interacts with your watchOS app’s user interface through , which are instances of a [`WKInterfaceObject`](https://developer.apple.com/documentation/watchkit/wkinterfaceobject) subclass. Interface objects are not views, but proxy objects for the actual views presented by your watchOS app. The WatchKit framework provides interface objects for most of the items you can add to your storyboard.

Communication between an interface object and the corresponding view on Apple Watch is one-way: information flows from your code to the view. In other words, you set values on an interface object but you cannot get the view’s current values. If you need to access the current value, you must cache that value in your code.

To create an interface object, add an item to a scene in your storyboard. Then open the assistant editor and control-drag the item from the storyboard into the scene’s interface controller ([`Figure 1`](https://developer.apple.com/documentation/watchkit/storyboard_support/building_watchos_app_interfaces_using_the_storyboard/connecting_your_user_interface_to_your_code#3172422)).

Xcode then prompts you for the outlet’s name. Enter a name and click Connect ([`Figure 2`](https://developer.apple.com/documentation/watchkit/storyboard_support/building_watchos_app_interfaces_using_the_storyboard/connecting_your_user_interface_to_your_code#3144653)).

Xcode then adds an outlet for the interface object, connecting it to the item in your storyboard.

```swift
// MARK: - Outlets

@IBOutlet weak var firstButton: WKInterfaceButton!
```

For more information on creating outlets, see [`Send Messages to a UI object`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devc06f7ee11).

When the system loads your interface controller, it automatically instantiates and configures the interface objects for all of your connected outlets. You never instantiate the interface objects. However, you can use these outlets to modify the item’s attributes at runtime.

You can configure interface elements in Xcode at design time, or you can use a connected interface object at runtime. However, interface objects often only expose a subset of the attributes available in Xcode’s Attributes inspector.

For example, the [`WKInterfaceLabel`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel) class exposes methods to set the text (or attributed text) and text color at runtime:

- [`setText(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settext(_:))
- [`setTextColor(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settextcolor(_:))
- [`setAttributedText(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/setattributedtext(_:))

Additional properties, such as minimum scale, number of lines, and alignment, are only available in the Attributes inspector at design time ([`Figure 3`](https://developer.apple.com/documentation/watchkit/storyboard_support/building_watchos_app_interfaces_using_the_storyboard/connecting_your_user_interface_to_your_code#3148615)).

Additionally, each scene in your storyboard file must contain all of the interface elements you intend to use. While you cannot add or remove items from the interface at runtime, you can hide items that you don’t currently need. This effectively removes these items from the interface, as the system treats hidden objects as if you had removed them from the storyboard.

To hide or show an item at runtime, call its [`setHidden(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sethidden(_:)) method.

Controls—such as buttons, sliders, and pickers—let the user interact with your app. To respond to user interactions, you must connect the control to an action method in your scene’s interface controller. Control-drag from the control to your interface controller in the assistant editor to create a Connection to Action ([`Figure 4`](https://developer.apple.com/documentation/watchkit/storyboard_support/building_watchos_app_interfaces_using_the_storyboard/connecting_your_user_interface_to_your_code#3148596)).

After you enter the name and click Connect, Xcode adds an action method to your interface controller, and connects it to the control. The method’s signature depends on the type of control. For example, a button’s action method doesn’t take any arguments, while a picker’s action method takes an integer, representing the index of the selected item.

```swift
    // MARK: - Action Methods
    
    @IBAction func buttonActionMethod() {
    }
    
    @IBAction func switchActionMethod(_ value: Bool) {
    }
    
    @IBAction func sliderActionMethod(_ value: Float) {
    }
    
    @IBAction func pickerActionMethod(_ value: Int) {
    }
```

The system automatically calls the connected action method whenever the user interacts with the control, giving your app a chance to react. For more information, see [`Receiving messages from a UI object`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev9662c7670).

## Code Examples

### Example

```swift
// MARK: - Outlets

@IBOutlet weak var firstButton: WKInterfaceButton!
```

### Example

```swift
// MARK: - Action Methods
    
    @IBAction func buttonActionMethod() {
    }
    
    @IBAction func switchActionMethod(_ value: Bool) {
    }
    
    @IBAction func sliderActionMethod(_ value: Float) {
    }
    
    @IBAction func pickerActionMethod(_ value: Int) {
    }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/connecting-your-user-interface-to-your-code)*