# UITraitDefinition

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A type representing a trait in a trait collection.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@protocol UITraitDefinition
```

## Mentions

- [Providing data to the view hierarchy with custom traits](./providing-data-to-the-view-hierarchy-with-custom-traits.md)

## Overview

All traits contained in a [`UITraitCollection`](./uitraitcollection.md) conform to this protocol. Three protocols refine `UITraitDefinition`: [`UINSIntegerTraitDefinition`](./uinsintegertraitdefinition.md), [`UICGFloatTraitDefinition`](./uicgfloattraitdefinition.md), or [`UIObjectTraitDefinition`](./uiobjecttraitdefinition.md). You can create custom traits by defining your own object conforming one of these three protocols, as appropriate for your trait value.

The example below defines a new trait that holds an [`NSInteger`](../ObjectiveC/nsinteger.md) value:

```objc
typedef NS_ENUM(NSInteger, Theme) {
    ThemeStandard,
    ThemeMonochrome
};

@interface MyThemeTrait : NSObject<UINSIntegerTraitDefinition>
@end

@implementation MyThemeTrait
+ (NSInteger)defaultValue { return ThemeStandard; }
@end
```

Defining [`defaultValue`](./uitraitdefinition-64c15/defaultvalue.md) is the minimum requirement to conform to this protocol. The [`defaultValue`](./uitraitdefinition-64c15/defaultvalue.md) must be constant.

The best candidates for trait values are simple scalars: [`NSInteger`](../ObjectiveC/nsinteger.md) and [`CGFloat`](../CoreFoundation/cgfloat-swift.struct.md). You can also use lightweight objects as trait values, but these are less efficient than simple scalars. Examples of lightweight objects include [`NSString`](../Foundation/nsstring.md), [`NSDate`](../Foundation/nsdate.md), or a composite of similarly lightweight objects. Make sure the default value never changes, preferably by making the object immutable. The system frequently checks trait values for equality, so classes need an efficient implementation of [`isEqual(_:)`](../ObjectiveC/nsobjectprotocol/isequal%28_%29.md).

If you use your custom trait to implement custom dynamic colors, implement [`affectsColorAppearance`](./uitraitdefinition-64c15/affectscolorappearance.md) and return `YES`. Returning `YES` tells the system to update and redraw views automatically when the trait changes. The system responds to changes to your trait similar to changes in system traits contained in [`systemTraitsAffectingColorAppearance`](./uitraitcollection/systemtraitsaffectingcolorappearance-64z7q.md). Changes to traits that affect color appearance are more expensive, so opt in to this behavior only when necessary, and change such traits infrequently.

A trait type serves as a unique key, identifying a trait within a trait collection. Methods such as [`valueForNSIntegerTrait:`](./uitraitcollection/valuefornsintegertrait_.md) and [`registerForTraitChanges:withHandler:`](./uitraitchangeobservable-7qoet/registerfortraitchanges_withhandler_.md) take a trait type to identify the trait in a collection.

### Traits in both Swift and Objective-C

If you need to access traits from both Swift and Objective-C code, create a type conforming to [`UITraitDefinition`](./uitraitdefinition-64c15.md) in both languages. To define a trait that’s accessible from both Swift and Objective-C, follow these guidelines :

- In Swift, define a structure that conforms to [`UITraitDefinition`](./uitraitdefinition-64c15.md).
- In Objective-C, define an [`NSObject`](../ObjectiveC/nsobject-swift.class.md) subclass that conforms to [`UINSIntegerTraitDefinition`](./uinsintegertraitdefinition.md), [`UICGFloatTraitDefinition`](./uicgfloattraitdefinition.md), or [`UIObjectTraitDefinition`](./uiobjecttraitdefinition.md).
- Implement [`defaultValue`](./uitraitdefinition-64c15/defaultvalue.md), [`name`](./uitraitdefinition-64c15/name.md), and [`identifier`](./uitraitdefinition-64c15/identifier.md), and make the values the same in Objective-C and Swift.
- If your trait holds an object value, make the class visible to both Swift and Objective-C.
- If your trait holds a fundamental value type, make your Objective-C types correspond to Swift types, as in the following table:

| Swift | Objective-C |
| --- | --- |
| [`Bool`](../Swift/bool.md) | [`NSInteger`](../ObjectiveC/nsinteger.md) |
| [`Int`](../Swift/int.md) | [`NSInteger`](../ObjectiveC/nsinteger.md) |
| [`Double`](../Swift/double.md) | [`CGFloat`](../CoreFoundation/cgfloat-swift.struct.md) |
| [`CGFloat`](../CoreFoundation/cgfloat-swift.struct.md) | [`CGFloat`](../CoreFoundation/cgfloat-swift.struct.md) |

For Swift [`Bool`](../Swift/bool.md) values, Objective-C uses 0 for `false` and 1 for `true`.

If your Swift trait uses an optional type for the [`defaultValue`](./uitraitdefinition-64c15/defaultvalue.md), Objective-C represents a Swift `nil` value with a special Objective-C constant. The table below lists the Objective-C values that correspond to a Swift `nil` value.

| Swift optional type | Swift value | Objective-C type | Objective-C value |
| --- | --- | --- | --- |
| `Int?` | `nil` | [`NSInteger`](../ObjectiveC/nsinteger.md) | [`NSNotFound`](../Foundation/nsnotfound-4qp9h.md) |
| `Double?` | `nil` | [`CGFloat`](../CoreFoundation/cgfloat-swift.struct.md) | [`CGFLOAT_MAX`](../CoreFoundation/cgfloat_max.md) |
| `CGFloat?` | `nil` | [`CGFloat`](../CoreFoundation/cgfloat-swift.struct.md) | [`CGFLOAT_MAX`](../CoreFoundation/cgfloat_max.md) |

In Objective-C, your trait value may require an [`NSObject`](../ObjectiveC/nsobject-swift.class.md) subclass if your data model exceeds the simple scalars of [`NSInteger`](../ObjectiveC/nsinteger.md) and [`CGFloat`](../CoreFoundation/cgfloat-swift.struct.md). To use this value in Swift, import your Objective-C class into Swift, and use it for the value of your custom trait in both languages. Other than bridging with Objective-C, avoid using reference types for Swift trait values.

You can prevent Swift from importing your Objective-C class name by applying the `NS_REFINED_FOR_SWIFT` macro to your Objective-C interface. This macro allows you to name your Swift trait structure with the same name as your Objective-C trait class.

The example below defines a trait in Objective-C, with a custom `Theme` type for a trait value.

```objc
typedef NS_ENUM(NSInteger, Theme) {
    ThemeStandard,
    ThemeMonochrome
};

NS_REFINED_FOR_SWIFT @interface ThemeTrait : NSObject<UINSIntegerTraitDefinition>
@end

@implementation ThemeTrait
+ (NSInteger)defaultValue { return ThemeStandard; }
+ (NSString *)name { return @"Theme"; }
+ (NSString *)identifier { return @"com.example.themetrait"; }
@end

```

The following code example shows the definition of a Swift trait so that UIKit recognizes it as the same trait as defined above in Objective-C:

```swift
// The NS_REFINED_FOR_SWIFT macro allows this struct to have 
// the same name as the Objective-C trait class.
struct ThemeTrait: UITraitDefinition {
    static let defaultValue = Theme.standard
    static let name = "Theme"
    static let identifier = "com.example.themetrait"
}
```

The `NS_REFINED_FOR_SWIFT` macro makes your Objective-C class available in Swift by prepending double underscores to the class name. You can use this to make your Swift implementation call your Objective-C class properties. For more details, refer to [Improving Objective-C API Declarations for Swift](../Swift/improving-objective-c-api-declarations-for-swift.md).

## Topics

### Type Properties
- [affectsColorAppearance](./uitraitdefinition-3572h/affectscolorappearance.md)
  Whether the trait is used to resolve dynamic colors (or images), and changes to the trait should automatically trigger views using dynamic colors/images to update their appearance. Default is NO.
- [identifier](./uitraitdefinition-3572h/identifier.md)
  A unique identifier string for the trait (reverse-DNS format recommended). Allows the trait to be encoded/decoded, and to map both a Swift and Objective-C trait to the same data.
- [name](./uitraitdefinition-3572h/name.md)
  A short human-readable name for the trait, e.g. for printing and debugging output. By default, the trait’s class name is used when not implemented.

## Relationships

### Inherited By
- [UICGFloatTraitDefinition](./uicgfloattraitdefinition.md)
- [UINSIntegerTraitDefinition](./uinsintegertraitdefinition.md)
- [UIObjectTraitDefinition](./uiobjecttraitdefinition.md)

## See Also

### Custom traits
- [Providing data to the view hierarchy with custom traits](./providing-data-to-the-view-hierarchy-with-custom-traits.md)
  Share data that needs to flow hierarchically across multiple levels of your view hierarchy.
- [UITrait](./uitrait-1dbah.md)
- [UIObjectTraitDefinition](./uiobjecttraitdefinition.md)
- [UICGFloatTraitDefinition](./uicgfloattraitdefinition.md)
- [UINSIntegerTraitDefinition](./uinsintegertraitdefinition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitdefinition-3572h)*