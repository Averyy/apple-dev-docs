# UIViewController.ViewLoading

**Framework**: UIKit  
**Kind**: struct

A property wrapper that loads the view controller’s view before accessing the property.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst ?+
- tvOS 16.4+
- visionOS ?+
- Swift 5.1+

## Declaration

```swift
@propertyWrapper
struct ViewLoading<Value>
```

#### Overview

Use this property wrapper on view controller properties that can be `nil` before the view controller’s view loads. Wrapping view controller properties this way eliminates crashes that can occur from implicitly defining properties as [`Optional`](https://developer.apple.com/documentation/Swift/Optional), and then referencing them before the view controller finishes loading.

The following example uses the [`UIViewController.ViewLoading`](uiviewcontroller/viewloading.md) wrapper to ensure that `dateLabel` [`UILabel`](uilabel.md) loads before referencing it in the `didSet` of the `date` property observer:

```swift
class DateViewController: UIViewController {
    @ViewLoading private var dateLabel: UILabel
    
    var date: Date? {
        didSet {
            let dateFormatter = DateFormatter()
            dateFormatter.dateStyle = .full
            let dateString = dateFormatter.string(from: self.date ?? Date())
            // If the view controller's view hasn't loaded yet,
            // accessing the dateLabel property here causes it to load.
            self.dateLabel.text = dateString
        }
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        let label = UILabel(frame: self.view.bounds)
        self.view.addSubview(label)
        self.dateLabel = label
    }
}
```

After loading [`UILabel`](uilabel.md), the system can safely access and set the `date` property.

```swift
let dateViewController = DateViewController()
dateViewController.date = Date()
```

Use this property wrapper over implicitly unwrapped optionals for `IBOutlets` as well.

```swift
@IBOutlet @ViewLoading private var dateLabel: UILabel
```

## Topics

### Creating a ViewLoading property wrapper
- [init()](uiviewcontroller/viewloading/init.md)
  Creates an empty property wrapper that loads the view controller’s view before accessing the property.
- [init(wrappedValue: Value)](uiviewcontroller/viewloading/init(wrappedvalue:).md)
  Creates a property wrapper that loads the view controller’s view before accessing the property.

## See Also

- [func updateProperties()](uiviewcontroller/updateproperties.md)
  Configures the view controller’s content and styling properties.
- [func updatePropertiesIfNeeded()](uiviewcontroller/updatepropertiesifneeded.md)
  Forces an immediate properties update for this view controller and its view, including any view controllers and views in this subtree.
- [func setNeedsUpdateProperties()](uiviewcontroller/setneedsupdateproperties.md)
  Call to manually request a properties update for the view controller. Multiple requests may be coalesced into a single update alongside the next layout pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/viewloading)*