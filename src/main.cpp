#include <wx/wxprec.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include <wx/aboutdlg.h>

#include "mainframe.hpp"


class MLAatKST : public wxApp {
    public:
        virtual bool OnInit();
};

wxIMPLEMENT_APP(MLAatKST);

bool MLAatKST::OnInit() {
    
    this->SetAppDisplayName(wxT("MLAatKST"));

    MainFrame* window = new MainFrame(wxT("MLAatKST"));
    window->Show();

    return true;
}
