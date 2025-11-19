# Packages to add

* pnpm (needed for vtsls)
* vtsls (typescript LSP implementation)
* basedpyright
* Sublime's standalone VS Code LSPs
  * Sublime is doing the best job at keeping a standalone version of VSCode's LSPs up-to-date
  * Unfortunately, they use a different Markdown server based on .Net, which would not be straightforward to package
  * https://github.com/sublimelsp/LSP-css
  * https://github.com/sublimelsp/LSP-json
  * https://github.com/sublimelsp/LSP-html
  * https://github.com/sublimelsp/LSP-eslint
* dua (TUI disk usage analyzer)

# Deleting a package from the local repo

Once you no longer have a need to build a particular package locally, you need
to delete it from the appropriate local apk repo, or else
`./cbuild bulk-pkg status:outdated` will keep building it.

There's hopefully an easier way to do this, but here's what I did.

In my case, I wanted to stop building `main/borg`.
I used [this cbuild source code](https://github.com/chimera-linux/cports/blob/172eff501015856ec83395580ed2b1234425a7bd/src/cbuild/apk/cli.py#L434-L449)
as a reference for how `apk mkndx` is used.

```nushell
cd ~/cports
let repo = "main"
let pkgToRemove = "borg"
let signingKey = "./etc/keys/key.rsa"
let arch = "x86_64"
let pkgsPath = $"packages/($repo)/($arch)/"
let pkgs = (
	apk --arch $arch --root bldroot/ --repository $"packages/($repo)/" search --from none
	| split row "\n"
	| where {|pkg| if ($pkg starts-with $pkgToRemove) { print $"Removing ($pkg)"; false} else { true } }
)
let pkgPaths = (
	$pkgs
	| each { [ $pkgsPath, $in, ".apk"] | str join }
)

let packagesAdbPath = $"($pkgsPath)/Packages.adb"
let oldPackagesAdbPath = $"($pkgsPath)/Packages.adb.old"
let apkindexPath = $"($pkgsPath)/APKINDEX.tar.gz"

mv  $packagesAdbPath $oldPackagesAdbPath
apk mkndx --output $packagesAdbPath --hash sha256-160 --index $oldPackagesAdbPath --sign-key $signingKey ...$pkgPaths
rm $apkindexPath
ln $packagesAdbPath $apkindexPath

print $"New list of built packages in the ($repo) repository:"
print ($pkgs)
```
