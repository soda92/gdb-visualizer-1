#include <windows.h>

void ErrorExit() {
  // Retrieve the system error message for the last-error code

  LPVOID lpMsgBuf;
  DWORD dw = GetLastError();

  if (FormatMessage(FORMAT_MESSAGE_ALLOCATE_BUFFER |
                        FORMAT_MESSAGE_FROM_SYSTEM |
                        FORMAT_MESSAGE_IGNORE_INSERTS,
                    NULL, dw, MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
                    (LPTSTR)&lpMsgBuf, 0, NULL) == 0) {
    MessageBox(NULL, TEXT("FormatMessage failed"), TEXT("Error"), MB_OK);
    ExitProcess(dw);
  }

  MessageBox(NULL, (LPCTSTR)lpMsgBuf, TEXT("Error"), MB_OK);

  LocalFree(lpMsgBuf);
  ExitProcess(dw);
}

int main() {
  // Generate an error

  if (!GetProcessId(NULL))
    ErrorExit();
}