// k2/py/cc/k2.cc

// Copyright (c)  2020  Fangjun Kuang (csukuangfj@gmail.com)

// See ../../../LICENSE for clarification regarding multiple authors

#include "k2/py/cc/k2.h"

#include "k2/py/cc/array.h"
#include "k2/py/cc/fsa.h"
#include "k2/py/cc/fsa_util.h"

PYBIND11_MODULE(_k2, m) {
  m.doc() = "pybind11 binding of k2";
  PybindArc(m);
  PybindArray(m);
  PybindFsa(m);
  PybindFsaUtil(m);
}
