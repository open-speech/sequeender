// sequeender/cc/fsa.cc

// Copyright (c)  2020  Daniel Povey
//                      Fangjun Kuang (csukuangfj@gmail.com)

// See ../../LICENSE for clarification regarding multiple authors

#include "sequeender/cc/fsa.h"
#include <algorithm>

namespace {

// 64-byte alignment should be enough for AVX512 and other computations.
constexpr std::size_t kAlignment = 64;
static_assert((kAlignment & 15) == 0,
              "kAlignment should be at least multiple of 16");
static_assert(kAlignment % alignof(sequeender::Arc) == 0, "");

inline std::size_t AlignTo(std::size_t b, std::size_t alignment) {
  // alignment should be power of 2
  return (b + alignment - 1) & (~(alignment - 1));
}

}  // namespace

namespace sequeender {

std::vector<Point> NearestNeighbors::Nearest(Point point, int k) {
  sort(points.begin(), points.end(), [point](Point a, Point b) {
    // Not concerned with actual distances, so skip the sqrt
    auto norm_a =
        (a.x - point.x) * (a.x - point.x) + (a.y - point.y) * (a.y - point.y);

    auto norm_b =
        (b.x - point.x) * (b.x - point.x) + (b.y - point.y) * (b.y - point.y);

    return norm_a < norm_b;
  });

  auto k_nearest = std::vector<Point>(points.begin(), points.begin() + k);
  return k_nearest;
}

std::ostream &operator<<(std::ostream &os, const Arc &arc) {
  os << arc.src_state << " " << arc.dest_state << " " << arc.label;
  return os;
}

std::ostream &operator<<(std::ostream &os, const Fsa &fsa) {
  os << "num_states: " << fsa.NumStates() << "\n";
  os << "num_arcs: " << fsa.size2 << "\n";
  for (const auto &arc : fsa) {
    os << arc << "\n";
  }
  return os;
}

}  // namespace sequeender
