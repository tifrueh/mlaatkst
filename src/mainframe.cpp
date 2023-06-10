#include <wx/wxprec.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include <wx/aboutdlg.h>

#include "id.hpp"
#include "mainframe.hpp"
#include "quotation_formatter.hpp"


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
    menuFile->Append(wxID_CLOSE, wxT("&Close Window\tCtrl-w"));
 
    wxMenu *menuHelp = new wxMenu;
    menuHelp->Append(wxID_ABOUT, wxT("&About MLAatKST\tCtrl-?"));
 
    wxMenuBar *menuBar = new wxMenuBar;
    menuBar->Append(menuFile, "&File");
    menuBar->Append(menuHelp, "&Help");

    this->SetMenuBar(menuBar);

    Bind(wxEVT_MENU, &MainFrame::OnQuit, this, wxID_EXIT);
    Bind(wxEVT_MENU, &MainFrame::OnClose, this, wxID_CLOSE);
    Bind(wxEVT_MENU, &MainFrame::OnAbout, this, wxID_ABOUT);
    Bind(wxEVT_RADIOBOX, &MainFrame::OnRadioBox, this, winID::ID_RADIOBOX);
    Bind(wxEVT_BUTTON, &MainFrame::OnOK, this, wxID_OK);
    Bind(wxEVT_BUTTON, &MainFrame::OnClear, this, winID::ID_CLEAR);

    showDialogue();
}

wxAboutDialogInfo MainFrame::GetInfo() {
    return info;
}

void MainFrame::OnClose(wxCommandEvent& event) {
    Close();
}

void MainFrame::OnAbout(wxCommandEvent& event) {
    wxAboutBox(GetInfo(), this);
}

void MainFrame::OnQuit(wxCommandEvent& event) {
    Close();
}

void MainFrame::OnClear(wxCommandEvent& event) {
    clearAllInputs();
}

void MainFrame::OnRadioBox(wxCommandEvent& event) {
    switch (radioBox->GetSelection()) {
        case 0:
            hideAllInputs();
            showInputGroupZero();
            clearAllInputs();
            break;
        
        case 1:
            hideAllInputs();
            showInputGroupOne();
            clearAllInputs();
            break;
        
        case 2:
            hideAllInputs();
            showInputGroupTwo();
            clearAllInputs();
            break;
    };
}

void MainFrame::OnOK(wxCommandEvent& event) {
    switch (radioBox->GetSelection()) {
        case 0:
            getInputGroupZero();
            resultS = qft::bookFirstQuotation(authorNameS, titleS, subtitleS, editionS, publisherS, locationS, yearS, pageSS);
            break;
        
        case 1:
            getInputGroupOne();
            resultS = qft::bookSecondQuotation(authorLastNameS, yearS, pageSS);
            break;
        
        case 2:
            getInputGroupTwo();
            resultS = qft::web(authorNameS, titleS, subtitleS, urlS, dateS);
            break;
    };

    result->SetLabel(resultS);
    topsizer->Layout();
}

void MainFrame::showDialogue() {
    appTitle = new wxStaticText(this, wxID_ANY, wxT("MLA Standart an der KST"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL);
    wxFont titleFont = appTitle->GetFont();
    titleFont.Scale(2);
    titleFont.MakeBold();
    appTitle->SetFont(titleFont);

    wxArrayString radioBoxOptions;
    radioBoxOptions.Add(wxT("&Erstnennung Buch"));
    radioBoxOptions.Add(wxT("&Zweitnennung Buch"));
    radioBoxOptions.Add(wxT("&Webzitat"));
    radioBox = new wxRadioBox(this, winID::ID_RADIOBOX, wxT("Optionen"), wxDefaultPosition, wxDefaultSize, radioBoxOptions, 3, wxRA_SPECIFY_COLS);

    authorName = new wxStaticText(this, wxID_ANY, wxT("Name des Autors / der Autorin: (Nachname, Vorname)"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    authorLastName = new wxStaticText(this, wxID_ANY, wxT("Nachname des Autors / der Autorin:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    title = new wxStaticText(this, wxID_ANY, wxT("Titel des Werks:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    subtitle = new wxStaticText(this, wxID_ANY, wxT("Untertitel: (leer lassen wenn nicht vorhanden)"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    edition = new wxStaticText(this, wxID_ANY, wxT("Auflage: (Zahl eingeben)"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    publisher = new wxStaticText(this, wxID_ANY, wxT("Verlag"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    location = new wxStaticText(this, wxID_ANY, wxT("Ort"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    year = new wxStaticText(this, wxID_ANY, wxT("Jahr"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    pageS = new wxStaticText(this, wxID_ANY, wxT("Zitierte Seite(n):"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    url = new wxStaticText(this, wxID_ANY, wxT("URL:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    date = new wxStaticText(this, wxID_ANY, wxT("Herunterladedatum:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);

    authorNameCtrl = new wxTextCtrl(this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize(250, wxDefaultSize.GetY()));
    authorLastNameCtrl = new wxTextCtrl(this, wxID_ANY);
    titleCtrl = new wxTextCtrl(this, wxID_ANY);
    subtitleCtrl = new wxTextCtrl(this, wxID_ANY);
    editionCtrl = new wxTextCtrl(this, wxID_ANY);
    publisherCtrl = new wxTextCtrl(this, wxID_ANY);
    locationCtrl = new wxTextCtrl(this, wxID_ANY);
    yearCtrl = new wxTextCtrl(this, wxID_ANY);
    pageSCtrl = new wxTextCtrl(this, wxID_ANY);
    urlCtrl = new wxTextCtrl(this, wxID_ANY);
    dateCtrl = new wxTextCtrl(this, wxID_ANY);

    buttonOK = new wxButton(this, wxID_OK);

    inputSizer = new wxFlexGridSizer(2, 0, 20);
    inputSizer->AddGrowableCol(1);
    inputSizer->Add(authorName, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(authorNameCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(authorLastName, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(authorLastNameCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(title, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(titleCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(subtitle, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(subtitleCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(edition, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(editionCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(publisher, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(publisherCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(location, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(locationCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(year, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(yearCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(pageS, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(pageSCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(url, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(urlCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(date, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(dateCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->AddStretchSpacer();
    inputSizer->Add(buttonOK, 0, wxALIGN_CENTER | wxALL, 5);

    result = new wxStaticText(this, wxID_ANY, wxT("Das Resultat erscheint hier ..."), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER);

    buttonCopy = new wxButton(this, wxID_ANY, wxT("Fussnote kopieren"));
    buttonReset = new wxButton(this, winID::ID_CLEAR, wxT("Felder zurücksetzen"));

    buttonSizer = new wxBoxSizer(wxHORIZONTAL);
    buttonSizer->Add(buttonCopy, 1, wxCENTER | wxALL, 10);
    buttonSizer->Add(buttonReset, 1, wxCENTER | wxALL, 10);

    topsizer = new wxBoxSizer(wxVERTICAL);

    topsizer->Add(
        appTitle,
        0,
        wxEXPAND |
        wxALL,
        10
    );

    topsizer->Add(
        radioBox,
        0,
        wxALIGN_CENTRE |
        wxBOTTOM | wxLEFT | wxRIGHT,
        10
    );

    topsizer->Add(
        inputSizer,
        1,
        wxEXPAND |
        wxALL,
        10
    );

    topsizer->Add(
        result,
        0,
        wxEXPAND |
        wxALL,
        10
    );

    topsizer->Add(
        buttonSizer,
        0,
        wxEXPAND |
        wxALL,
        10
    );

    hideAllInputs();
    showInputGroupZero();

    SetSizerAndFit(topsizer);
}

void MainFrame::hideAllInputs() {
    inputSizer->Show(authorName, false);
    inputSizer->Show(authorNameCtrl, false);
    inputSizer->Show(authorLastName, false);
    inputSizer->Show(authorLastNameCtrl, false);
    inputSizer->Show(title, false);
    inputSizer->Show(titleCtrl, false);
    inputSizer->Show(subtitle, false);
    inputSizer->Show(subtitleCtrl, false);
    inputSizer->Show(edition, false);
    inputSizer->Show(editionCtrl, false);
    inputSizer->Show(publisher, false);
    inputSizer->Show(publisherCtrl, false);
    inputSizer->Show(location, false);
    inputSizer->Show(locationCtrl, false);
    inputSizer->Show(year, false);
    inputSizer->Show(yearCtrl, false);
    inputSizer->Show(pageS, false);
    inputSizer->Show(pageSCtrl, false);
    inputSizer->Show(url, false);
    inputSizer->Show(urlCtrl, false);
    inputSizer->Show(date, false);
    inputSizer->Show(dateCtrl, false);
    inputSizer->Layout();
}

void MainFrame::showInputGroupZero() {
    inputSizer->Show(authorName);
    inputSizer->Show(authorNameCtrl);
    inputSizer->Show(title);
    inputSizer->Show(titleCtrl);
    inputSizer->Show(subtitle);
    inputSizer->Show(subtitleCtrl);
    inputSizer->Show(edition);
    inputSizer->Show(editionCtrl);
    inputSizer->Show(publisher);
    inputSizer->Show(publisherCtrl);
    inputSizer->Show(location);
    inputSizer->Show(locationCtrl);
    inputSizer->Show(year);
    inputSizer->Show(yearCtrl);
    inputSizer->Show(pageS);
    inputSizer->Show(pageSCtrl);
    inputSizer->Layout();
}

void MainFrame::showInputGroupOne() {
    inputSizer->Show(authorLastName);
    inputSizer->Show(authorLastNameCtrl);
    inputSizer->Show(year);
    inputSizer->Show(yearCtrl);
    inputSizer->Show(pageS);
    inputSizer->Show(pageSCtrl);
    inputSizer->Layout();
}

void MainFrame::showInputGroupTwo() {
    inputSizer->Show(authorName);
    inputSizer->Show(authorNameCtrl);
    inputSizer->Show(title);
    inputSizer->Show(titleCtrl);
    inputSizer->Show(subtitle);
    inputSizer->Show(subtitleCtrl);
    inputSizer->Show(url);
    inputSizer->Show(urlCtrl);
    inputSizer->Show(date);
    inputSizer->Show(dateCtrl);
    inputSizer->Layout();
}

void MainFrame::getInputGroupZero() {
    authorNameS = authorNameCtrl->GetLineText(0);
    titleS = titleCtrl->GetLineText(0);
    subtitleS = subtitleCtrl->GetLineText(0);
    editionS = editionCtrl->GetLineText(0);
    publisherS = publisherCtrl->GetLineText(0);
    locationS = locationCtrl->GetLineText(0);
    yearS = yearCtrl->GetLineText(0);
    pageSS = pageSCtrl->GetLineText(0);
}

void MainFrame::getInputGroupOne() {
    authorLastNameS = authorLastNameCtrl->GetLineText(0);
    yearS = yearCtrl->GetLineText(0);
    pageSS = pageSCtrl->GetLineText(0);
}

void MainFrame::getInputGroupTwo() {
    authorNameS = authorNameCtrl->GetLineText(0);
    titleS = titleCtrl->GetLineText(0);
    subtitleS = subtitleCtrl->GetLineText(0);
    urlS = urlCtrl->GetLineText(0);
    dateS = dateCtrl->GetLineText(0);
}

void MainFrame::clearAllInputs() {
    authorNameCtrl->Clear();
    authorLastNameCtrl->Clear();
    titleCtrl->Clear();
    subtitleCtrl->Clear();
    editionCtrl->Clear();
    publisherCtrl->Clear();
    locationCtrl->Clear();
    yearCtrl->Clear();
    pageSCtrl->Clear();
    urlCtrl->Clear();
    dateCtrl->Clear();
}
