let
  pkgs = import <nixpkgs> { };
in
pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.selenium
      python-pkgs.numpy
      python-pkgs.flake8
    ]))
  ];
}
