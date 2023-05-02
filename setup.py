from setuptools import setup, find_packages

setup(name="limit-order-book",
      description="Matching Engine",
      url="https://github.com/naoki-test1/matching_engine_for_crypto/",
      version="0.0.1",
      author="naoki",
      author_email="user@user.com",
      license="MIT",
      packages=find_packages(exclude=["tests"]),
      platforms="any",
      scripts=["bin/script_runner.py", "bin/benchmark.py", "bin/threaded_script.py"],
      classifiers=[
        "python3", "trade", "exchange",
        "order-book", "limit-order-book"
        "multi-threading", "batches", "mongodb", "transactions"],
      python_requires=">=3.0")
