# SwiftUI updates

**Framework**: Updates

Learn about important changes to SwiftUI.

#### Overview

Browse notable changes in [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI).

#### June 2025

##### General

- Apply Liquid Glass effects to views using [`glassEffect(_:in:isEnabled:)`](https://developer.apple.com/documentation/SwiftUI/View/glassEffect(_:in:isEnabled:)).
- Use [`glass`](https://developer.apple.com/documentation/SwiftUI/PrimitiveButtonStyle/glass) with the [`buttonStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/buttonStyle(_:)-66fbx) modifier to apply Liquid Glass to instances of `Button`.
- [`ToolbarSpacer`](https://developer.apple.com/documentation/SwiftUI/ToolbarSpacer) creates a visual break between items in toolbars containing Liquid Glass.
- Use [`scrollEdgeEffectStyle(_:for:)`](https://developer.apple.com/documentation/SwiftUI/View/scrollEdgeEffectStyle(_:for:)) to configure the scroll edge effect style for scroll views.
- [`backgroundExtensionEffect()`](https://developer.apple.com/documentation/SwiftUI/View/backgroundExtensionEffect()) duplicates, mirrors, and blurs views placed around edges with available safe areas.
- Set behavior for tab bar minimization with [`tabBarMinimizeBehavior(_:)`](https://developer.apple.com/documentation/SwiftUI/View/tabBarMinimizeBehavior(_:)).
- Set the [`search`](https://developer.apple.com/documentation/SwiftUI/TabRole/search) role on a tab to take someone to a search tab and have a search field take the place of the tab bar.
- Adjust the content of accessory views based on the placement in a tab view with [`TabViewBottomAccessoryPlacement`](https://developer.apple.com/documentation/SwiftUI/TabViewBottomAccessoryPlacement).
- Connect a [`WebView`](https://developer.apple.com/documentation/WebKit/WebView-swift.struct) with a [`WebPage`](https://developer.apple.com/documentation/WebKit/WebPage) to fully control the browsing experience in your app.
- Drag multiple items using the [`draggable(_:_:)`](https://developer.apple.com/documentation/SwiftUI/View/draggable(_:_:)) modifier. Make a view a container for draggable views using the [`dragContainer(for:id:in:selection:_:)`](https://developer.apple.com/documentation/SwiftUI/View/dragContainer(for:id:in:selection:_:)) modifier.
- Use the [`Animatable()`](https://developer.apple.com/documentation/SwiftUI/Animatable()) macro to have SwiftUI synthesize custom animatable data properties.
- [`Slider`](https://developer.apple.com/documentation/SwiftUI/Slider) now supports tick marks. Tick marks appear automatically when initializing a `Slider` with the `step` parameter.
- Use [`windowResizeAnchor(_:)`](https://developer.apple.com/documentation/SwiftUI/View/windowResizeAnchor(_:)) to set the window anchor point when a window must resize.

##### Text

- [`TextEditor`](https://developer.apple.com/documentation/SwiftUI/TextEditor) now supports [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString).
- Handle text selection with attributed text using [`AttributedTextSelection`](https://developer.apple.com/documentation/SwiftUI/AttributedTextSelection).
- [`AttributedTextFormattingDefinition`](https://developer.apple.com/documentation/SwiftUI/AttributedTextFormattingDefinition) defines how text can be styled in specific contexts.
- Use [`FindContext`](https://developer.apple.com/documentation/SwiftUI/FindContext) to create a find navigator in views that support text editing.

##### Accessibility

- Support Assistive Access in iOS and iPadOS scenes with [`AssistiveAccess`](https://developer.apple.com/documentation/SwiftUI/AssistiveAccess).

##### Hdr

- [`Color.ResolvedHDR`](https://developer.apple.com/documentation/SwiftUI/Color/ResolvedHDR) is a set of RGBA values that represent a color that can be shown, including HDR headroom information.

##### Uikit and Appkit Integration

- Host and present SwiftUI scenes in UIKit with [`UIHostingSceneDelegate`](https://developer.apple.com/documentation/SwiftUI/UIHostingSceneDelegate) and in AppKit with [`NSHostingSceneRepresentation`](https://developer.apple.com/documentation/SwiftUI/NSHostingSceneRepresentation).
- Incorporate gesture recognizers in SwiftUI views from AppKit with [`NSGestureRecognizerRepresentable`](https://developer.apple.com/documentation/SwiftUI/NSGestureRecognizerRepresentable).

##### Immersive Spaces

- Manipulate views using common hand gestures with [`manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)`](https://developer.apple.com/documentation/SwiftUI/View/manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)).
- Snap volumes to horizontal surfaces and windows to vertical surfaces using [`SurfaceSnappingInfo`](https://developer.apple.com/documentation/SwiftUI/SurfaceSnappingInfo).
- Use [`RemoteImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/RemoteImmersiveSpace) to render stereo content from your Mac app on Apple Vision Pro.
- Use [`SpatialContainer`](https://developer.apple.com/documentation/SwiftUI/SpatialContainer) to create a layout container that aligns overlapping content in 3D space.
- Depth-based variants of modifiers allow easier volumetric layouts in SwiftUI. For example, [`aspectRatio3D(_:contentMode:)`](https://developer.apple.com/documentation/SwiftUI/View/aspectRatio3D(_:contentMode:)), [`rotation3DLayout(_:)`](https://developer.apple.com/documentation/SwiftUI/View/rotation3DLayout(_:)), and [`depthAlignment(_:)`](https://developer.apple.com/documentation/SwiftUI/Layout/depthAlignment(_:)).

#### June 2024

##### Volumes

- Specify the alignment of a volume when moved in the world using the [`volumeWorldAlignment(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/volumeWorldAlignment(_:)) scene modifier.
- Specify the default world scaling behavior of your scene using the [`defaultWorldScaling(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/defaultWorldScaling(_:)) scene modifier.
- Adjust the visibilty of a volume’s baseplate using the [`volumeBaseplateVisibility(_:)`](https://developer.apple.com/documentation/SwiftUI/View/volumeBaseplateVisibility(_:)) view modifier.
- Define a custom action to execute when the viewpoint of a volume changes using the [`onVolumeViewpointChange(updateStrategy:initial:_:)`](https://developer.apple.com/documentation/SwiftUI/View/onVolumeViewpointChange(updateStrategy:initial:_:)) view modifier.

##### Windows

- Change the default initial size and position of a window using the [`defaultWindowPlacement(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/defaultWindowPlacement(_:)) modifier.
- Change the default behavior for how windows behave when performing a zoom using [`WindowIdealSize`](https://developer.apple.com/documentation/SwiftUI/WindowIdealSize) and provide the placement for the zoomed window with the [`windowIdealPlacement(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/windowIdealPlacement(_:)) modifier.
- Create utility windows in SwiftUI using the new [`UtilityWindow`](https://developer.apple.com/documentation/SwiftUI/UtilityWindow) scene type and toggle the window’s visibility using the [`WindowVisibilityToggle`](https://developer.apple.com/documentation/SwiftUI/WindowVisibilityToggle).
- Customize the style of a window using the new [`window`](https://developer.apple.com/documentation/SwiftUI/ContainerBackgroundPlacement/window) container background placement, the [`toolbar(removing:)`](https://developer.apple.com/documentation/SwiftUI/View/toolbar(removing:)) view modifier, and the [`plain`](https://developer.apple.com/documentation/SwiftUI/WindowStyle/plain) window style.
- Set the default launch behavior for a scene using the [`defaultLaunchBehavior(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/defaultLaunchBehavior(_:)) modifier.
- Replace one scene with another using the [`pushWindow`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/pushWindow) method.

##### Immersive Spaces

- Add an action to perform when the state of the immersion changes using the [`onImmersionChange(_:)`](https://developer.apple.com/documentation/SwiftUI/View/onImmersionChange(_:)) modifier.
- Apply a custom color or dim a passthrough video in an immersive space using the [`colorMultiply(_:)`](https://developer.apple.com/documentation/SwiftUI/SurroundingsEffect/colorMultiply(_:)) and [`dim(intensity:)`](https://developer.apple.com/documentation/SwiftUI/SurroundingsEffect/dim(intensity:)) initializers.

##### Documents

- Customize the launch experience of document-based applications using [`DocumentGroupLaunchScene`](https://developer.apple.com/documentation/SwiftUI/DocumentGroupLaunchScene) and [`NewDocumentButton`](https://developer.apple.com/documentation/SwiftUI/NewDocumentButton).

##### Navigation

- Specify the appearance and interaction of [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView) with the [`tabViewStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/tabViewStyle(_:))  modifier using values like [`sidebarAdaptable`](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/sidebarAdaptable), [`tabBarOnly`](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/tabBarOnly), and [`grouped`](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/grouped).
- Build hierarchy by nesting tabs as a tab item within [`TabSection`](https://developer.apple.com/documentation/SwiftUI/TabSection).
- Enable people to customize a [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView) using the [`tabViewCustomization(_:)`](https://developer.apple.com/documentation/SwiftUI/View/tabViewCustomization(_:)) modifier and persist customization state in [`AppStorage`](https://developer.apple.com/documentation/SwiftUI/AppStorage) with [`TabViewCustomization`](https://developer.apple.com/documentation/SwiftUI/TabViewCustomization).

##### Modal Presentations

- Use built-in presentation sizes for sheets like [`form`](https://developer.apple.com/documentation/SwiftUI/PresentationSizing/form) or [`page`](https://developer.apple.com/documentation/SwiftUI/PresentationSizing/page) with the [`presentationSizing(_:)`](https://developer.apple.com/documentation/SwiftUI/View/presentationSizing(_:)) modifier or create custom sized sheets using the [`PresentationSizing`](https://developer.apple.com/documentation/SwiftUI/PresentationSizing) protocol.

##### Toolbars

- Specify the display mode of toolbars in macOS using the [`ToolbarLabelStyle`](https://developer.apple.com/documentation/SwiftUI/ToolbarLabelStyle) type.
- Configure the foreground style in the toolbar environment in watchOS using the [`toolbarForegroundStyle(_:for:)`](https://developer.apple.com/documentation/SwiftUI/View/toolbarForegroundStyle(_:for:)) view modifier.
- Anchor ornaments relative to the depth of your volume — in addition to the height and width — using the [`scene(_:)`](https://developer.apple.com/documentation/SwiftUI/OrnamentAttachmentAnchor/scene(_:)-1l8wf) method that takes a [`UnitPoint3D`](https://developer.apple.com/documentation/SwiftUI/UnitPoint3D).

##### Views

- Create custom container views like [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker), [`List`](https://developer.apple.com/documentation/SwiftUI/List), and [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView) using new [`Group`](https://developer.apple.com/documentation/SwiftUI/Group) and [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach) initializers, like [`init(subviews:transform:)`](https://developer.apple.com/documentation/SwiftUI/Group/init(subviews:transform:)) and [`init(subviews:content:)`](https://developer.apple.com/documentation/SwiftUI/ForEach/init(subviews:content:)), respectively.
- Declare a custom container value by defining a key that conforms to the [`ContainerValueKey`](https://developer.apple.com/documentation/SwiftUI/ContainerValueKey) protocol, and set the container value for a view using the [`containerValue(_:_:)`](https://developer.apple.com/documentation/SwiftUI/View/containerValue(_:_:)) modifier.
- Create [`EnvironmentValues`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues), [`Transaction`](https://developer.apple.com/documentation/SwiftUI/Transaction), [`ContainerValues`](https://developer.apple.com/documentation/SwiftUI/ContainerValues), and [`FocusedValues`](https://developer.apple.com/documentation/SwiftUI/FocusedValues) entries by using the [`Entry()`](https://developer.apple.com/documentation/SwiftUI/Entry()) macro to the variable declaration.

##### Animation

- Customize the transition when pushing a view onto a navigation stack or presenting a view with the [`navigationTransition(_:)`](https://developer.apple.com/documentation/SwiftUI/View/navigationTransition(_:)) view modifier.
- Add new symbols effects and configurations like [`wiggle`](https://developer.apple.com/documentation/Symbols/SymbolEffect/wiggle), [`rotate`](https://developer.apple.com/documentation/Symbols/SymbolEffect/rotate), and [`breathe`](https://developer.apple.com/documentation/Symbols/SymbolEffect/breathe) using the [`symbolEffect(_:options:value:)`](https://developer.apple.com/documentation/SwiftUI/View/symbolEffect(_:options:value:)) modifier.

##### Text Input and Output

- Add text suggestions support to any text field using [`textInputSuggestions(_:)`](https://developer.apple.com/documentation/SwiftUI/View/textInputSuggestions(_:)) and [`textInputCompletion(_:)`](https://developer.apple.com/documentation/SwiftUI/View/textInputCompletion(_:)) view modifiers.
- Access and modify selected text using a new [`TextSelection`](https://developer.apple.com/documentation/SwiftUI/TextSelection) binding for [`TextField`](https://developer.apple.com/documentation/SwiftUI/TextField) and [`TextEditor`](https://developer.apple.com/documentation/SwiftUI/TextEditor).
- Bind to the focus state of an app’s search field using the [`searchFocused(_:equals:)`](https://developer.apple.com/documentation/SwiftUI/View/searchFocused(_:equals:)) view modifier.

##### Drawing and Graphics

- Precompile shaders at build time using the [`compile(as:)`](https://developer.apple.com/documentation/SwiftUI/Shader/compile(as:)) method.
- Create mesh gradients with a grid of points and colors using the new [`MeshGradient`](https://developer.apple.com/documentation/SwiftUI/MeshGradient) type.
- Extend SwiftUI Text views with custom rendering effects and interaction behaviors using [`TextAttribute`](https://developer.apple.com/documentation/SwiftUI/TextAttribute), [`Text.Layout`](https://developer.apple.com/documentation/SwiftUI/Text/Layout), and [`TextRenderer`](https://developer.apple.com/documentation/SwiftUI/TextRenderer).
- Create a new [`Color`](https://developer.apple.com/documentation/SwiftUI/Color) by mixing two colors using the [`mix(with:by:in:)`](https://developer.apple.com/documentation/SwiftUI/Color/mix(with:by:in:)) method.

##### Layout

- Enable custom spacing between views in a [`ZStack`](https://developer.apple.com/documentation/SwiftUI/ZStack) along the depth axis with the [`init(alignment:spacing:content:)`](https://developer.apple.com/documentation/SwiftUI/ZStack/init(alignment:spacing:content:)) initializer.

##### Scrolling

- Scroll to a view, offset, or edge in a scroll view using the [`scrollPosition(_:anchor:)`](https://developer.apple.com/documentation/SwiftUI/View/scrollPosition(_:anchor:)) view modifier and specifying one of the [`ScrollPosition`](https://developer.apple.com/documentation/SwiftUI/ScrollPosition) values.
- Limit the number of views that can be scrolled by a single interaction using the limit behavior value [`alwaysByFew`](https://developer.apple.com/documentation/SwiftUI/ViewAlignedScrollTargetBehavior/LimitBehavior/alwaysByFew) or [`alwaysByOne`](https://developer.apple.com/documentation/SwiftUI/ViewAlignedScrollTargetBehavior/LimitBehavior/alwaysByOne).
- Add an action to be called when a view crosses a provided threshold using the [`onScrollVisibilityChange(threshold:_:)`](https://developer.apple.com/documentation/SwiftUI/View/onScrollVisibilityChange(threshold:_:)) modifier.
- Access both the old and new values when a scroll view’s phase changes by using the [`onScrollPhaseChange(_:)`](https://developer.apple.com/documentation/SwiftUI/View/onScrollPhaseChange(_:)-7mica) modifier.

##### Gestures

- Conditionally disable a gesture using the `isEnabled` parameter in a modifier like [`gesture(_:isEnabled:)`](https://developer.apple.com/documentation/SwiftUI/View/gesture(_:isEnabled:)).
- Create extra drag areas of a window in macOS when you add a [`WindowDragGesture`](https://developer.apple.com/documentation/SwiftUI/WindowDragGesture) gesture.
- Create a hand gesture shortcut for Double Tap in watchOS using the [`HandGestureShortcut`](https://developer.apple.com/documentation/SwiftUI/HandGestureShortcut) structure.
- Enable whether gestures can handle events that activate the containing window using the [`allowsWindowActivationEvents(_:)`](https://developer.apple.com/documentation/SwiftUI/View/allowsWindowActivationEvents(_:)) view modifier.

##### Input Events

- Create a group of hover effects that activate together using [`HoverEffectGroup`](https://developer.apple.com/documentation/SwiftUI/HoverEffectGroup) and apply them to a view using the [`hoverEffect(in:isEnabled:body:)`](https://developer.apple.com/documentation/SwiftUI/View/hoverEffect(in:isEnabled:body:)) view modifier.
- Customize the appearance of the system pointer in macOS, iPadOS, and visionOS with new pointer styles using [`pointerStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/pointerStyle(_:)) or the visibility with the [`pointerVisibility(_:)`](https://developer.apple.com/documentation/SwiftUI/View/pointerVisibility(_:)) modifier.
- Access keyboard modifier flags using the [`onModifierKeysChanged(mask:initial:_:)`](https://developer.apple.com/documentation/SwiftUI/View/onModifierKeysChanged(mask:initial:_:)).
- Replace the primary view with one or more alternative views when pressing a specified set of modifier keys using the [`modifierKeyAlternate(_:_:)`](https://developer.apple.com/documentation/SwiftUI/View/modifierKeyAlternate(_:_:)) view modifier.
- Enable the hand pointer for custom drawing and markup applications using the [`handPointerBehavior(_:)`](https://developer.apple.com/documentation/SwiftUI/View/handPointerBehavior(_:)) modifier.

##### Previews in Xcode

- Write dynamic properties inline in previews using the new [`Previewable()`](https://developer.apple.com/documentation/SwiftUI/Previewable()) macro.
- Inject shared environment objects, model containers, or other dependencies into previews using the [`PreviewModifier`](https://developer.apple.com/documentation/SwiftUI/PreviewModifier) protocol.

##### Accessibility

- Specify that your accessibility element behaves as a tab bar using the [`isTabBar`](https://developer.apple.com/documentation/SwiftUI/AccessibilityTraits/isTabBar) accessibility trait with the [`accessibilityAddTraits(_:)`](https://developer.apple.com/documentation/SwiftUI/View/accessibilityAddTraits(_:)) modifier. In UIKit, use [`tabBar`](https://developer.apple.com/documentation/UIKit/UIAccessibilityTraits/tabBar).
- Generate a localized description of a color in a string interpolation by adding `accessibilityName:`, such as `"\(accessibilityName: myColor)"`. Pass that string to any accessibility modifier.

##### Framework Interoperability

- Reuse existing UIKit gesture recognizer code in SwiftUI. In SwiftUI, create UIKit gesture recognizers using [`UIGestureRecognizerRepresentable`](https://developer.apple.com/documentation/SwiftUI/UIGestureRecognizerRepresentable). In UIKit, refer to SwiftUI gestures by name using [`name`](https://developer.apple.com/documentation/UIKit/UIGestureRecognizer/name).
- Share menu content definitions between SwiftUI and AppKit by using the [`NSHostingMenu`](https://developer.apple.com/documentation/SwiftUI/NSHostingMenu) in your AppKit view hierarchy.

#### June 2023 Visionos

##### Scenes

- Create a volume that can display 3D models by applying the [`volumetric`](https://developer.apple.com/documentation/SwiftUI/WindowStyle/volumetric) window style to an app’s window.
- Make use of a Full Space by opening an [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace) scene. You can use the [`mixed`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/mixed) immersion style to place objects in a person’s surroundings, or the [`full`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/full) style to completely control the visual experience.
- Display 3D models in a volume or a Full Space using RealityKit entities that you load with that framework’s [`Model3D`](https://developer.apple.com/documentation/RealityKit/Model3D) or [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) structure.

##### Toolbars and Ornaments

- Display a toolbar item in an ornament using the [`bottomOrnament`](https://developer.apple.com/documentation/SwiftUI/ToolbarItemPlacement/bottomOrnament) toolbar item placement.
- Add an ornament to a window directly using the [`ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`](https://developer.apple.com/documentation/SwiftUI/View/ornament(visibility:attachmentAnchor:contentAlignment:ornament:)) view modifier.

##### Drawing and Graphics

- Detect view geometry in three dimensions using a [`GeometryReader3D`](https://developer.apple.com/documentation/SwiftUI/GeometryReader3D).
- Add a 3D visual effect using the [`visualEffect3D(_:)`](https://developer.apple.com/documentation/SwiftUI/View/visualEffect3D(_:)) view modifier.
- Rotate or scale in three dimensions with view modifiers like [`rotation3DEffect(_:anchor:)`](https://developer.apple.com/documentation/SwiftUI/View/rotation3DEffect(_:anchor:)) and [`scaleEffect(x:y:z:anchor:)`](https://developer.apple.com/documentation/SwiftUI/View/scaleEffect(x:y:z:anchor:)), respectively.
- Convert between display points and physical distances using a [`PhysicalMetricsConverter`](https://developer.apple.com/documentation/SwiftUI/PhysicalMetricsConverter).

##### View Configuration

- Add a glass background effect to a view using the [`glassBackgroundEffect(displayMode:)`](https://developer.apple.com/documentation/SwiftUI/View/glassBackgroundEffect(displayMode:)) view modifier.
- Dim passthrough when appropriate by applying a [`preferredSurroundingsEffect(_:)`](https://developer.apple.com/documentation/SwiftUI/View/preferredSurroundingsEffect(_:)) modifier.

##### View Layout

- Make 3D adjustments to layout with view modifiers like [`offset(z:)`](https://developer.apple.com/documentation/SwiftUI/View/offset(z:)), [`padding3D(_:)`](https://developer.apple.com/documentation/SwiftUI/View/padding3D(_:)-6bex4), and [`frame(depth:alignment:)`](https://developer.apple.com/documentation/SwiftUI/View/frame(depth:alignment:)).

##### Gestures

- Enable people to rotate objects in three dimensions when you add a [`RotateGesture3D`](https://developer.apple.com/documentation/SwiftUI/RotateGesture3D) gesture.

#### June 2023

##### Scenes

- Close windows by their identifier using the [`dismissWindow`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/dismissWindow) action stored in the environment.
- Enable people to open a settings window by presenting a [`SettingsLink`](https://developer.apple.com/documentation/SwiftUI/SettingsLink) button.

##### Navigation

- Control views of a navigation split view or stack using a new overload of the [`navigationDestination(item:destination:)`](https://developer.apple.com/documentation/SwiftUI/View/navigationDestination(item:destination:)) view modifier.
- Manage column visibility of a navigation split view using new overloads of the view’s initializer, like [`init(columnVisibility:preferredCompactColumn:sidebar:content:detail:)`](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView/init(columnVisibility:preferredCompactColumn:sidebar:content:detail:)).

##### Modal Presentations

- Use new overloads of the file export, import, and move modifiers, like [`fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)`](https://developer.apple.com/documentation/SwiftUI/View/fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)-34bd6), to access new file management features. For example, you can: - Configure a file import or export dialog to open on a default directory, enable only certain file types, display hidden files, and so on.
- Retain file interface configuration that a person chooses from one presentation to the next.
- Export types that conform to the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol.
- Specify a dialog severity using the [`dialogSeverity(_:)`](https://developer.apple.com/documentation/SwiftUI/View/dialogSeverity(_:)) view modifier.
- Provide a custom icon for a dialog using the [`dialogIcon(_:)`](https://developer.apple.com/documentation/SwiftUI/View/dialogIcon(_:)) modifier.
- Enable people to suppress dialogs using one of the dialog suppression modifiers, like [`dialogSuppressionToggle(isSuppressed:)`](https://developer.apple.com/documentation/SwiftUI/View/dialogSuppressionToggle(isSuppressed:)).

##### Toolbars

- Configure the toolbar title display size using the [`toolbarTitleDisplayMode(_:)`](https://developer.apple.com/documentation/SwiftUI/View/toolbarTitleDisplayMode(_:)) modifier.

##### Search

- Present search programmatically using a binding to a new `isPresented` parameter available in some searchable view modifiers, like [`searchable(text:isPresented:placement:prompt:)`](https://developer.apple.com/documentation/SwiftUI/View/searchable(text:isPresented:placement:prompt:)-1hn4y).
- Create mutable search tokens by providing a binding to the input of the `token` closure in the applicable searchable view modifiers, like [`searchable(text:editableTokens:isPresented:placement:prompt:token:)`](https://developer.apple.com/documentation/SwiftUI/View/searchable(text:editableTokens:isPresented:placement:prompt:token:)-2ilmg).

##### Data and Storage

- Bridge between SwiftUI environment keys and UIKit traits more easily using the [`UITraitBridgedEnvironmentKey`](https://developer.apple.com/documentation/SwiftUI/UITraitBridgedEnvironmentKey) protocol.
- Get better performance when you share data throughout your app by using the new [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro.
- Access both the old and new values of a value that changes when processing the completion closure of the [`onChange(of:initial:_:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:initial:_:)-4psgg) view modifier.

##### Views

- Display a standard interface when a resource, like search results or a network connection, isn’t available using the [`ContentUnavailableView`](https://developer.apple.com/documentation/SwiftUI/ContentUnavailableView) view type.
- Display a standard inspector interface with a platform-appropriate appearance by applying the [`inspector(isPresented:content:)`](https://developer.apple.com/documentation/SwiftUI/View/inspector(isPresented:content:)) modifier.

##### Animation

- Perform an action when an animation completes by specifying a completion closure to the [`withAnimation(_:completionCriteria:_:completion:)`](https://developer.apple.com/documentation/SwiftUI/withAnimation(_:completionCriteria:_:completion:)) view modifier.
- Define custom animation behaviors by creating a type that conforms to the [`CustomAnimation`](https://developer.apple.com/documentation/SwiftUI/CustomAnimation) protocol.
- Perform animations that progress through predefined phases using the [`PhaseAnimator`](https://developer.apple.com/documentation/SwiftUI/PhaseAnimator) structure, or according to a set of time-based keyframes by using the [`Keyframes`](https://developer.apple.com/documentation/SwiftUI/Keyframes) protocol.
- Specify information about a change in state — for example, to request a particular animation — using custom [`TransactionKey`](https://developer.apple.com/documentation/SwiftUI/TransactionKey) instances.
- Design custom animation curves using [`UnitCurve`](https://developer.apple.com/documentation/SwiftUI/UnitCurve).
- Apply streamlined spring parameters, now standardized across all Apple frameworks, using the new [`spring(duration:bounce:blendDuration:)`](https://developer.apple.com/documentation/SwiftUI/Animation/spring(duration:bounce:blendDuration:)) animation. You can also use the [`Spring`](https://developer.apple.com/documentation/SwiftUI/Spring) structure as a convenience to represent a spring’s motion.

##### Text Input and Output

- Indicate the language that appears in a specific [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) view so that SwiftUI can help to avoid clipping and collision of text, and perform proper line breaking and hyphenation using the [`typesettingLanguage(_:isEnabled:)`](https://developer.apple.com/documentation/SwiftUI/View/typesettingLanguage(_:isEnabled:)-4ldzm) view modifier.
- Scale text semantically, for example by labeling it as having a secondary text scale, using the [`textScale(_:isEnabled:)`](https://developer.apple.com/documentation/SwiftUI/View/textScale(_:isEnabled:)) modifier.

##### Shapes

- Apply more than one [`fill(_:style:)`](https://developer.apple.com/documentation/SwiftUI/Shape/fill(_:style:)-3y2ud) or [`stroke(_:style:antialiased:)`](https://developer.apple.com/documentation/SwiftUI/Shape/stroke(_:style:antialiased:)) modifier to a single [`Shape`](https://developer.apple.com/documentation/SwiftUI/Shape).
- Apply Boolean operations to both shapes and paths, like [`intersection(_:eoFill:)`](https://developer.apple.com/documentation/SwiftUI/Shape/intersection(_:eoFill:)) and [`union(_:eoFill:)`](https://developer.apple.com/documentation/SwiftUI/Shape/union(_:eoFill:)).
- Use predefined shape styles, like [`rect`](https://developer.apple.com/documentation/SwiftUI/Shape/rect), to simplify your code.
- Create rounded rectangles with uneven corners using [`rect(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)`](https://developer.apple.com/documentation/SwiftUI/Shape/rect(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)).

##### Drawing and Graphics

- Create fully customizable, high-performance graphics by drawing with Metal shaders inside a SwiftUI app using a [`Shader`](https://developer.apple.com/documentation/SwiftUI/Shader) structure.
- Configure an image with a specific dynamic range by applying the [`allowedDynamicRange(_:)`](https://developer.apple.com/documentation/SwiftUI/View/allowedDynamicRange(_:)) view modifier.
- Compose effects that you apply to a view based on some aspect of the geometry of the view using the [`visualEffect(_:)`](https://developer.apple.com/documentation/SwiftUI/View/visualEffect(_:)) modifier. For example, you can apply a blur that varies depending on the view’s position in the display.

##### Layout

- Define custom coordinate spaces using the [`CoordinateSpaceProtocol`](https://developer.apple.com/documentation/SwiftUI/CoordinateSpaceProtocol) with new [`GeometryProxy`](https://developer.apple.com/documentation/SwiftUI/GeometryProxy) methods, like [`bounds(of:)`](https://developer.apple.com/documentation/SwiftUI/GeometryProxy/bounds(of:)) and [`frame(in:)`](https://developer.apple.com/documentation/SwiftUI/GeometryProxy/frame(in:)-68tks), to get the dimensions of containers.
- Create a frame for a view that lays out its content based on characteristics of the container view using [`containerRelativeFrame(_:alignment:)`](https://developer.apple.com/documentation/SwiftUI/View/containerRelativeFrame(_:alignment:)).
- Set the background of a container view using the [`containerBackground(_:for:)`](https://developer.apple.com/documentation/SwiftUI/View/containerBackground(_:for:)) view modifier.

##### Lists and Tables

- Disable selectability of an item in a [`List`](https://developer.apple.com/documentation/SwiftUI/List) or [`Table`](https://developer.apple.com/documentation/SwiftUI/Table) by applying the [`selectionDisabled(_:)`](https://developer.apple.com/documentation/SwiftUI/View/selectionDisabled(_:)) modifier.
- Collapse or expand a [`Section`](https://developer.apple.com/documentation/SwiftUI/Section) of a list or table using the `isExpanded` binding in the section’s initializer.
- Configure row or section spacing using the [`listRowSpacing(_:)`](https://developer.apple.com/documentation/SwiftUI/View/listRowSpacing(_:)) and [`listSectionSpacing(_:)`](https://developer.apple.com/documentation/SwiftUI/View/listSectionSpacing(_:)-5t518) modifiers, respectively.
- Set the prominence of a badge using the [`badgeProminence(_:)`](https://developer.apple.com/documentation/SwiftUI/View/badgeProminence(_:)) view modifier.
- Configure alternating row backgrounds using the [`alternatingRowBackgrounds(_:)`](https://developer.apple.com/documentation/SwiftUI/View/alternatingRowBackgrounds(_:)) modifier.
- Customize table column visibility and reordering using the [`TableColumnCustomization`](https://developer.apple.com/documentation/SwiftUI/TableColumnCustomization) structure.
- Add hierarchical rows to a table using the [`DisclosureTableRow`](https://developer.apple.com/documentation/SwiftUI/DisclosureTableRow) structure, or recursively hierarchical rows using the [`OutlineGroup`](https://developer.apple.com/documentation/SwiftUI/OutlineGroup) structure.
- Hide table column headers using the [`tableColumnHeaders(_:)`](https://developer.apple.com/documentation/SwiftUI/View/tableColumnHeaders(_:)) modifier.

##### Scrolling

- Read the position of a scroll view using one of the scroll position modifiers, like [`scrollPosition(id:anchor:)`](https://developer.apple.com/documentation/SwiftUI/View/scrollPosition(id:anchor:)).
- Flash scroll indicators programmatically using a view modifier, like [`scrollIndicatorsFlash(onAppear:)`](https://developer.apple.com/documentation/SwiftUI/View/scrollIndicatorsFlash(onAppear:)).
- Clip scroll views in custom ways after disabling default clipping using the [`scrollClipDisabled(_:)`](https://developer.apple.com/documentation/SwiftUI/View/scrollClipDisabled(_:)) modifier.
- Create paged scroll views, aligned to either page or view boundaries, using the [`scrollTargetBehavior(_:)`](https://developer.apple.com/documentation/SwiftUI/View/scrollTargetBehavior(_:)) view modifier.
- Create custom scroll behaviors using the [`ScrollTargetBehavior`](https://developer.apple.com/documentation/SwiftUI/ScrollTargetBehavior) protocol.
- Control the insets of scrollable views using the [`safeAreaPadding(_:)`](https://developer.apple.com/documentation/SwiftUI/View/safeAreaPadding(_:)-5lh9p) and [`contentMargins(_:_:for:)`](https://developer.apple.com/documentation/SwiftUI/View/contentMargins(_:_:for:)-1lt8b) view modifiers.
- Add effects to views as they scroll on- and offscreen using one of the [`scrollTransition(_:axis:transition:)`](https://developer.apple.com/documentation/SwiftUI/View/scrollTransition(_:axis:transition:)) modifiers.
- Create a [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView) that supports vertical paging in watchOS by applying the [`verticalPage`](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/verticalPage) tab view style.

##### Gestures

- Make smoother transitions between gestures and animations by using a new [`velocity`](https://developer.apple.com/documentation/SwiftUI/DragGesture/Value/velocity) property on the values associated with certain gestures and a [`tracksVelocity`](https://developer.apple.com/documentation/SwiftUI/Transaction/tracksVelocity) property on [`Transaction`](https://developer.apple.com/documentation/SwiftUI/Transaction).
- Gain access to more information, including both velocity and position, by migrating to the new [`MagnifyGesture`](https://developer.apple.com/documentation/SwiftUI/MagnifyGesture) and [`RotateGesture`](https://developer.apple.com/documentation/SwiftUI/RotateGesture), which replace the now deprecated `MagnificationGesture` and `RotationGesture`.

##### Input Events

- Enable a view that’s in focus to react directly to keyboard input by applying one of the [`onKeyPress(_:action:)`](https://developer.apple.com/documentation/SwiftUI/View/onKeyPress(_:action:)) view modifiers.
- Enable people to choose from a compact collection of items in a [`Menu`](https://developer.apple.com/documentation/SwiftUI/Menu) by styling a [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker) with the [`palette`](https://developer.apple.com/documentation/SwiftUI/PickerStyle/palette) style.
- Provide haptic or audio feedback in response to an event using one of the sensory feedback modifiers, like [`sensoryFeedback(_:trigger:)`](https://developer.apple.com/documentation/SwiftUI/View/sensoryFeedback(_:trigger:)).
- Create buttons and toggles that perform an [`AppIntent`](https://developer.apple.com/documentation/AppIntents/AppIntent) in a widget, Live Activity, and other places using new initializers like [`init(_:intent:)`](https://developer.apple.com/documentation/SwiftUI/Button/init(_:intent:)-7urde) and [`init(_:isOn:intent:)`](https://developer.apple.com/documentation/SwiftUI/Toggle/init(_:isOn:intent:)-4lsrf).

##### Focus

- Distinguish between views for which focus serves different purposes, such as those that have a primary action like a button and those that take input like a text field, using the new [`focusable(_:interactions:)`](https://developer.apple.com/documentation/SwiftUI/View/focusable(_:interactions:)) view modifier.
- Manage the effect that receiving focus has on a view using the [`focusEffectDisabled(_:)`](https://developer.apple.com/documentation/SwiftUI/View/focusEffectDisabled(_:)) modifier.

##### Previews in Xcode

- Reduce the amount of boilerplate that you need to create Xcode previews by using the new [`Preview(_:traits:_:body:)`](https://developer.apple.com/documentation/SwiftUI/Preview(_:traits:_:body:)) macro.

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/swiftui)*