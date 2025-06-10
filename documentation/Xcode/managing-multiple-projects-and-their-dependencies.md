# Managing multiple projects and their dependencies

**Framework**: Xcode

Manage related projects in one place using a workspace, or configure build-time dependencies between different Xcode projects using cross-project references.

#### Overview

An Xcode project manages the code and resources associated with your company’s software products. Most projects are organized around a single product, but you can also use one project to manage multiple products. For example, a project might build an app, app extensions, and app-related frameworks. The organization of your projects affects how your teams work on those projects, and can also affect build performance.

Although you can use a single project for all of your company’s content, there are advantages to distributing content among multiple projects:

- Multiple smaller projects are easier to navigate. With fewer files, fewer targets, and fewer products in the project, it’s easier for you to navigate the project’s content and see what’s there.
- Multiple projects make it easier to distribute work. If you have multiple teams, giving each one a separate project makes it easier for them to work independently.
- Multiple independent projects can result in faster build times. Separating content into multiple, independent projects forces you to eliminate or minimize dependencies between those projects. When you limit dependencies, Xcode has more flexibility to build projects in parallel, rather than serially.

When you separate content into independent projects, there might still be dependencies between them. For example, if an app team and framework team are developing their content in tandem, they each need access to the latest changes from both projects. Workspaces and cross-project references help you manage these dependencies between projects.

##### Manage Multiple Related Projects Using a Workspace

A workspace is a container for several related projects. Use a workspace to organize multiple projects that have explicit or implicit dependencies. For example, you might use a workspace to organize one or more apps and the shared frameworks they link against.

To create a workspace and add projects to it:

1. In Xcode, choose File > New > Workspace.
2. Specify a name for the workspace and save it to the file system.
3. In the Project navigator, Control-click in the empty space and choose Add Files to “”.
4. In the sheet that appears, select an Xcode project (a file with a `.xcodeproj` filename extension).
5. Click Add to add the project to the workspace.

> **Note**: You can also add projects to a workspace by dragging them from the Finder to the Project navigator of your workspace window. Make sure you add each project at the root level of the workspace, not as a subproject of another project.

When you add projects to a workspace, Xcode automatically detects dependencies between the targets in those projects and builds them in the correct order. For example, when you build an app that implicitly depends on a framework in a different project, Xcode automatically builds the framework before it builds the app. When you change your project, Xcode automatically updates any dependencies, so you don’t have to change them manually.

##### Refer Explicitly to Targets Files and Products in Another Project

By default, a project in a workspace can’t refer to targets, files, or products in another project. If you need to refer to items in another project, you must create a cross-project reference:

1. Open your Project navigator in your Xcode project.
2. Click the Add button (+) at the bottom of the Project navigator.
3. Choose Add Files to “”.
4. Select another Xcode project (`.xcodeproj` filename extension) from the file dialog.
5. Click Add.

After you add a cross-project reference, you can refer to the other project’s targets, files, and products from your original project’s Dependencies, Copy Files, and Link Binary with Library build phases. If Xcode can’t locate the other project at build time, the build system still attempts to build the product but produces missing dependency warnings.

> **Note**: It’s good practice to use a workspace to manage multiple projects. However, you can’t create explicit dependencies between two projects in the same workspace.

## See Also

- [Managing files and folders in your Xcode project](managing-files-and-folders-in-your-xcode-project.md)
  Add new or existing files to your project, and use groups to organize the files and folders in the Project navigator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/managing-multiple-projects-and-their-dependencies)*