# dfint.github.io

The project's landing page localized to several languages

## Commands to work with the site localization

Push source template to transifex (`_template/index.md`):

```shell
tx push
```

Pull translated files from transifex:

```shell
tx pull --all --use-git-timestamps --minimum-perc 100
```
