#include <wx/wxprec.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include <wx/aboutdlg.h>


class MLAatKST : public wxApp {
    public:
        virtual bool OnInit();
        wxAboutDialogInfo GetInfo();
    
    private:
        wxAboutDialogInfo info;
};

class MainFrame : public wxFrame {
    public:
        MainFrame(wxString title);

    private:
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
};

wxIMPLEMENT_APP(MLAatKST);

bool MLAatKST::OnInit() {
    
    this->SetAppDisplayName(wxT("MLAatKST"));

    info.SetName(wxT("MLAatKST"));
    info.SetVersion(wxT("2.0.0-dev"));
    info.SetCopyright(wxT(
        "Copyright (C) 2022-2023 Timo Früh\n"
        "This program is free and open source software, licensed under the GNU General Public License 3.0. "
        "For futher information, see <https://www.gnu.org/licenses/>."
    ));

    MainFrame* window = new MainFrame(wxT("MLAatKST"));
    window->Show();

    return true;
}

wxAboutDialogInfo MLAatKST::GetInfo() {
    return info;
}

MainFrame::MainFrame(wxString title) : wxFrame(NULL, wxID_ANY, title) {
    wxMenu *menuFile = new wxMenu;
    menuFile->Append(wxID_EXIT, wxT("&Quit MLAatKST\tCtrl-q"));
 
    wxMenu *menuHelp = new wxMenu;
    menuHelp->Append(wxID_ABOUT, wxT("&About MLAatKST\tCtrl-?"));
 
    wxMenuBar *menuBar = new wxMenuBar;
    menuBar->Append(menuFile, "&File");
    menuBar->Append(menuHelp, "&Help");

    this->SetMenuBar(menuBar);

    Bind(wxEVT_MENU, &MainFrame::OnQuit, this, wxID_EXIT);
    Bind(wxEVT_MENU, &MainFrame::OnAbout, this, wxID_ABOUT);
}

void MainFrame::OnAbout(wxCommandEvent& event) {
    wxAboutBox(wxGetApp().GetInfo(), this);
}

void MainFrame::OnQuit(wxCommandEvent& event) {
    Close();
}
