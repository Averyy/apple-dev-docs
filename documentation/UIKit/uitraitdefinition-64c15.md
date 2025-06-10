# UITraitDefinition

**Framework**: UIKit  
**Kind**: protocol

A type representing a trait in a trait collection.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
protocol UITraitDefinition
```

#### Overview

All traits contained in a [`UITraitCollection`](uitraitcollection.md) conform to this protocol. You can create custom traits by defining your own conforming type.

The example below defines a new trait that holds the value of an integer-based enumeration named `Theme`:

```swift
enum Theme: Int {
    case standard
    case monochrome
}

struct ThemeTrait: UITraitDefinition {
    static let defaultValue = Theme.standard
}
```

The protocol defines default implementations for [`name`](uitraitdefinition-64c15/name.md) and [`identifier`](uitraitdefinition-64c15/identifier.md) properties. Defining [`defaultValue`](uitraitdefinition-64c15/defaultvalue.md) is the minimum requirement to conform to this protocol. All properties you implement must be constant. `UITraitDefinition` defines the associated type [`Value`](uitraitdefinition-64c15/value.md) which is the type of [`defaultValue`](uitraitdefinition-64c15/defaultvalue.md).

The best candidates for trait values are simple value types, such as [`Bool`](https://developer.apple.com/documentation/Swift/Bool), [`Int`](https://developer.apple.com/documentation/Swift/Int), [`Double`](https://developer.apple.com/documentation/Swift/Double), and enumerations with an [`Int`](https://developer.apple.com/documentation/Swift/Int) raw value. You can also use lightweight structures as trait values. The system frequently tests trait values for equality, so structures need an efficient implementation of `Equatable`. Avoid using Swift classes as trait values.

If you use your custom trait to implement custom dynamic colors, implement [`affectsColorAppearance`](uitraitdefinition-64c15/affectscolorappearance.md) and return `true`. Returning `true` tells the system to update and redraw views automatically when the trait changes. The system responds to changes to your trait similar to changes in system traits contained in [`systemTraitsAffectingColorAppearance`](uitraitcollection/systemtraitsaffectingcolorappearance-64z7q.md). Changes to traits that affect color appearance are more expensive, so opt in to this behavior only when necessary, and change such traits infrequently.

For each custom trait, define extensions on [`UIMutableTraits`](uimutabletraits-13ja5.md) and [`UITraitCollection`](uitraitcollection.md) to enable reading and modifying your custom traits with standard property syntax. The example below shows extensions for the example `Theme` trait.

```swift
extension UITraitCollection {
    var theme: Theme { self[ThemeTrait.self] }
}

extension UIMutableTraits {
    var theme: Theme {
        get { self[ThemeTrait.self] }
        set { self[ThemeTrait.self] = newValue }
    }
}
```

A trait type serves as a unique key, identifying a trait within a trait collection. Methods such as [`subscript(_:)`](uitraitcollection/subscript(_:)-6cdgq.md) and `UIPresentationController/registerForTraitChanges(_:handler:)` take a trait type to identify the trait in a collection.

Traits defined in Swift aren’t automatically bridged to Objective-C. If you need to access your custom trait from both Swift and Objective-C code, define the trait in both languages. For details, see the Objective-C documentation for [`UITraitDefinition`](uitraitdefinition-3572h.md).

## Topics

### Associated Types
- [associatedtype Value](uitraitdefinition-64c15/value.md)
### Type Properties
- [static var affectsColorAppearance: Bool](uitraitdefinition-64c15/affectscolorappearance.md)
- [static var defaultValue: Self.Value](uitraitdefinition-64c15/defaultvalue.md)
- [static var identifier: String](uitraitdefinition-64c15/identifier.md)
- [static var name: String](uitraitdefinition-64c15/name.md)

## Relationships

### Conforming Types
- [UITraitAccessibilityContrast](uitraitaccessibilitycontrast-swift.struct.md)
- [UITraitActiveAppearance](uitraitactiveappearance-swift.struct.md)
- [UITraitDisplayGamut](uitraitdisplaygamut-swift.struct.md)
- [UITraitDisplayScale](uitraitdisplayscale-swift.struct.md)
- [UITraitForceTouchCapability](uitraitforcetouchcapability-swift.struct.md)
- [UITraitHDRHeadroomUsageLimit](uitraithdrheadroomusagelimit-swift.struct.md)
- [UITraitHorizontalSizeClass](uitraithorizontalsizeclass-swift.struct.md)
- [UITraitImageDynamicRange](uitraitimagedynamicrange-swift.struct.md)
- [UITraitLayoutDirection](uitraitlayoutdirection-swift.struct.md)
- [UITraitLegibilityWeight](uitraitlegibilityweight-swift.struct.md)
- [UITraitListEnvironment](uitraitlistenvironment-swift.struct.md)
- [UITraitPreferredContentSizeCategory](uitraitpreferredcontentsizecategory-swift.struct.md)
- [UITraitSceneCaptureState](uitraitscenecapturestate-swift.struct.md)
- [UITraitSplitViewControllerLayoutEnvironment](uitraitsplitviewcontrollerlayoutenvironment-swift.struct.md)
- [UITraitTabAccessoryEnvironment](uitraittabaccessoryenvironment-swift.struct.md)
- [UITraitToolbarItemPresentationSize](uitraittoolbaritempresentationsize-swift.struct.md)
- [UITraitTypesettingLanguage](uitraittypesettinglanguage-swift.struct.md)
- [UITraitUserInterfaceIdiom](uitraituserinterfaceidiom-swift.struct.md)
- [UITraitUserInterfaceLevel](uitraituserinterfacelevel-swift.struct.md)
- [UITraitUserInterfaceStyle](uitraituserinterfacestyle-swift.struct.md)
- [UITraitVerticalSizeClass](uitraitverticalsizeclass-swift.struct.md)

## See Also

- [protocol UIMutableTraits](uimutabletraits-13ja5.md)
  A mutable container of traits.
- [typealias UITrait](uitrait-9423.md)
  A type representing a trait in a trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitdefinition-64c15)*