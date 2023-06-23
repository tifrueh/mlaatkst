#include <wx/wxprec.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include <wx/clipbrd.h>

#include "id.hpp"
#include "quotation_formatter.hpp"
#include "toppanel.hpp"

TopPanel::TopPanel(wxWindow* parent) : wxPanel(parent, wxID_ANY, wxDefaultPosition, wxDefaultSize) {
    appTitle = new wxStaticText(this, wxID_ANY, _("MLA at the KST"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL);
    wxFont titleFont = appTitle->GetFont();
    titleFont.Scale(2);
    titleFont.MakeBold();
    appTitle->SetFont(titleFont);

    wxArrayString radioBoxOptions;
    radioBoxOptions.Add(_("&First mention of a book"));
    radioBoxOptions.Add(_("&Second mention of a book"));
    radioBoxOptions.Add(_("&Mention of a website"));
    radioBox = new wxRadioBox(this, winID::ID_RADIOBOX, _("Options"), wxDefaultPosition, wxDefaultSize, radioBoxOptions, 3, wxRA_SPECIFY_COLS);

    authorName = new wxStaticText(this, wxID_ANY, _("Name of the author: (name, surname)"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    authorLastName = new wxStaticText(this, wxID_ANY, _("Last name of the author:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    title = new wxStaticText(this, wxID_ANY, _("Title:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    subtitle = new wxStaticText(this, wxID_ANY, _("Subtitle: (leave empty if there is none)"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    edition = new wxStaticText(this, wxID_ANY, _("Edition: (enter a number)"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    publisher = new wxStaticText(this, wxID_ANY, _("Publisher:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    location = new wxStaticText(this, wxID_ANY, _("Location:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    year = new wxStaticText(this, wxID_ANY, _("Year:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    pageS = new wxStaticText(this, wxID_ANY, _("Page(s) quoted:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    url = new wxStaticText(this, wxID_ANY, _("URL:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    date = new wxStaticText(this, wxID_ANY, _("Download date:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);

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

    resultS = _("The footnote appears here ...");

    result = new wxStaticText(this, wxID_ANY, resultS, wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER);

    buttonCopy = new wxButton(this, winID::ID_COPY, _("Copy footnote"));
    buttonReset = new wxButton(this, winID::ID_CLEAR, _("Reset inputs"));

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
    SetFocus();
}

void TopPanel::processRadioBox() {
    switch (radioBox->GetSelection()) {
        case 0:
            hideAllInputs();
            showInputGroupZero();
            break;
        
        case 1:
            hideAllInputs();
            showInputGroupOne();
            break;
        
        case 2:
            hideAllInputs();
            showInputGroupTwo();
            break;
    };
}

void TopPanel::processOK() {
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

void TopPanel::processCopy() {
    if (wxTheClipboard->Open()) {
        wxTheClipboard->SetData(new wxTextDataObject(resultS));
        wxTheClipboard->Close();
    }
}

void TopPanel::hideAllInputs() {
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

void TopPanel::showInputGroupZero() {
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

void TopPanel::showInputGroupOne() {
    inputSizer->Show(authorLastName);
    inputSizer->Show(authorLastNameCtrl);
    inputSizer->Show(year);
    inputSizer->Show(yearCtrl);
    inputSizer->Show(pageS);
    inputSizer->Show(pageSCtrl);
    inputSizer->Layout();
}

void TopPanel::showInputGroupTwo() {
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

void TopPanel::getInputGroupZero() {
    authorNameS = authorNameCtrl->GetLineText(0);
    titleS = titleCtrl->GetLineText(0);
    subtitleS = subtitleCtrl->GetLineText(0);
    editionS = editionCtrl->GetLineText(0);
    publisherS = publisherCtrl->GetLineText(0);
    locationS = locationCtrl->GetLineText(0);
    yearS = yearCtrl->GetLineText(0);
    pageSS = pageSCtrl->GetLineText(0);
}

void TopPanel::getInputGroupOne() {
    authorLastNameS = authorLastNameCtrl->GetLineText(0);
    yearS = yearCtrl->GetLineText(0);
    pageSS = pageSCtrl->GetLineText(0);
}

void TopPanel::getInputGroupTwo() {
    authorNameS = authorNameCtrl->GetLineText(0);
    titleS = titleCtrl->GetLineText(0);
    subtitleS = subtitleCtrl->GetLineText(0);
    urlS = urlCtrl->GetLineText(0);
    dateS = dateCtrl->GetLineText(0);
}

void TopPanel::clearAllInputs() {
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

void TopPanel::selectInputGroupZero() {
    radioBox->SetSelection(0);
    hideAllInputs();
    showInputGroupZero();
}

void TopPanel::selectInputGroupOne() {
    radioBox->SetSelection(1);
    hideAllInputs();
    showInputGroupOne();
}

void TopPanel::selectInputGroupTwo() {
    radioBox->SetSelection(2);
    hideAllInputs();
    showInputGroupTwo();
}
