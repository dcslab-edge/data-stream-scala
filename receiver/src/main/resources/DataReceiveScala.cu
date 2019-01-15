#include <assert.h>

#define __assert(condition) \
  if (!(condition)) { return; }


extern "C"
// test reduce kernel that sums elements
__global__ void long_map_errcount(int n, long* in, long* out){
  //const long ix = threadIdx.x + blockIdx.x * (long)blockDim.x;
  int ix = blockIdx.x * blockDim.x + threadIdx.x;
  if(ix<n){
    if(in[ix] > 100000)
      out[ix] = 0;
    else out[ix] = 1;
  }
}


extern "C"
__global__ void int_map_errcount(int n, int* in, int* out){
  int ix = blockIdx.x * blockDim.x + threadIdx.x;
  if(ix<n){
    if(in[ix]>=50 && in[ix]<80)
      out[ix] = 0;
    else
      out[ix] = 1;
  }
}

extern "C"
// test reduce kernel that sums elements
__global__ void sum(int *size, int *input, int *output, int *stage, int *totalStages) {
  const long ix = threadIdx.x + blockIdx.x * (long)blockDim.x;
  const int jump = 64 * 256;
  // if (ix == 0) printf("size: %d stage : %d totalStages : %d \n",*size, *stage, *totalStages);
  if (*stage == 0) {
    if (ix < *size) {
      assert(jump == blockDim.x * gridDim.x);
      int result = 0;
      for (long i = ix; i < *size; i += jump) {
        result += input[i];
      }
      input[ix] = result;
    }
  } else if (ix == 0) {
    const long count = (*size < (long)jump) ? *size : (long)jump;
    int result = 0;
    for (long i = 0; i < count; ++i) {
      result += input[i];
    }
    output[0] = result;
  }
}


extern "C"
// test reduce kernel that sums elements
__global__ void suml(int size, long *input, long *output, int stage, int totalStages) {
  const long ix = threadIdx.x + blockIdx.x * (long)blockDim.x;
  const int jump = 64 * 256;
  if (stage == 0) {
    if (ix < size) {
      assert(jump == blockDim.x * gridDim.x);
      long result = 0;
      for (long i = ix; i < size; i += jump) {
        result += input[i];
      }
      input[ix] = result;
    }
  } else if (ix == 0) {
    const long count = (size < (long)jump) ? size : (long)jump;
    long result = 0;
    for (long i = 0; i < count; ++i) {
      result += input[i];
    }
    output[0] = result;
  }
}


