#include <wx/wxprec.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include <wx/aboutdlg.h>

#include "mainframe.hpp"


MainFrame::MainFrame(wxString title) : wxFrame(NULL, wxID_ANY, title) {

    info.SetName(wxT("MLAatKST"));
    info.SetVersion(wxT("2.0.0-dev"));
    info.SetCopyright(wxT(
        "Copyright (C) 2022-2023 Timo Früh\n"
        "This program is free and open source software, licensed under the GNU General Public License 3.0. "
        "For futher information, see <https://www.gnu.org/licenses/>."
    ));

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

    showDialogue();
}

wxAboutDialogInfo MainFrame::GetInfo() {
    return info;
}

void MainFrame::OnAbout(wxCommandEvent& event) {
    wxAboutBox(GetInfo(), this);
}

void MainFrame::OnQuit(wxCommandEvent& event) {
    Close();
}

void MainFrame::showDialogue() {
    wxBoxSizer* topsizer = new wxBoxSizer(wxVERTICAL);

    topsizer->Add(
        new wxStaticText(this, -1, "MLA Standart an der KST", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL),
        1,
        wxEXPAND |
        wxALL,
        10 
    );
    
    SetSizerAndFit(topsizer);
}
