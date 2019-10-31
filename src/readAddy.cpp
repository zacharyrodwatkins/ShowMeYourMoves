#include <cstring>
#include <dirent.h>
#include <fstream>
#include <sstream>
#include <string>
#include <sys/uio.h>
#include <iostream>


int main(void) {
  uint64_t m_emuRAMAddressStart=0x7f8080000000;//0x7f8080000000;
  pid_t m_PID =15697;
  uint32_t offset =0;//0x80000000;
  struct iovec local[1];
  struct iovec remote[1];
  ssize_t nread;
  char buffer[1];
  int size = 1;
  uint64_t RAMAddress = m_emuRAMAddressStart + offset;


  local[0].iov_base = buffer;
  local[0].iov_len = size;
  remote[0].iov_base = (void*) RAMAddress;
  remote[0].iov_len = size;

while(1){
  nread = process_vm_readv(m_PID, local, 1, remote, 1, 0);
  for(int i=0; i<size; ++i)
    std::cout << std::hex << (int) buffer[i];
  std::cout  << " " <<nread << "\n";

  //int val = buff
  }
  return 0;
}