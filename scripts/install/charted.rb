class Charted < Formula
  desc "Native SVG chart generation library"
  homepage "https://github.com/marzukia/charted"
  url "https://github.com/marzukia/charted/archive/refs/tags/v1.0.2.tar.gz"
  sha256 "807561a4d55e0cc84f12b40c7988cc3f0fb36ff7f49ae7eab0b059c78f79c40d"
  license "MIT"

  depends_on "python@3.11"

  def install
    system "python3", "-m", "pip", "install", "--no-build-isolation", "-e", "."
    bin.install "bin/charted"
  end

  test do
    system "#{bin}/charted", "--version"
  end
end
