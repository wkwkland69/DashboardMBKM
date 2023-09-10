# Import library yang diperlukan
import csv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


# Fungsi untuk membaca data dari file CSV
def read_csv_file(filename):
    data = []
    with open(filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            nama_kpi = row["Id"]
            mssubclass = row["MSSubClass"]
            mszoning = row["MSZoning"]
            lotfrontage = row["LotFrontage"]
            lotarea = row["LotArea"]
            street = row["Street"]
            alley = row["Alley"]
            lotshape = row["LotShape"]
            landcontour = row["LandContour"]
            utilities = row["Utilities"]
            lotconfig = row["LotConfig"]
            landslope = row["LandSlope"]
            neighborhood = row["Neighborhood"]
            condition1 = row["Condition1"]
            condition2 = row["Condition2"]
            bldgtype = row["BldgType"]
            housestyle = row["HouseStyle"]
            overallqual = row["OverallQual"]
            overallcond = row["OverallCond"]
            yearbuilt = row["YearBuilt"]
            yearremodadd = row["YearRemodAdd"]
            roofstyle = row["RoofStyle"]
            roofmatl = row["RoofMatl"]
            exterior1st = row["Exterior1st"]
            exterior2nd = row["Exterior2nd"]
            masvnrtype = row["MasVnrType"]
            masvnrarea = row["MasVnrArea"]
            exterqual = row["ExterQual"]
            extercond = row["ExterCond"]
            foundation = row["Foundation"]
            bsmtqual = row["BsmtQual"]
            bsmtcond = row["BsmtCond"]
            bsmtexposure = row["BsmtExposure"]
            bsmtfintype1 = row["BsmtFinType1"]
            bsmtfinsf1 = row["BsmtFinSF1"]
            bsmtfintype2 = row["BsmtFinType2"]
            bsmtfinsf2 = row["BsmtFinSF2"]
            bsmtunfsf = row["BsmtUnfSF"]
            totalbsmtsf = row["TotalBsmtSF"]
            heating = row["Heating"]
            heatingqc = row["HeatingQC"]
            centralair = row["CentralAir"]
            electrical = row["Electrical"]
            firstflrsf = row["1stFlrSF"]
            secondflrsf = row["2ndFlrSF"]
            lowqualfinsf = row["LowQualFinSF"]
            grlivarea = row["GrLivArea"]
            bsmtfullbath = row["BsmtFullBath"]
            bsmthalfbath = row["BsmtHalfBath"]
            fullbath = row["FullBath"]
            halfbath = row["HalfBath"]
            bedroomabvgr = row["BedroomAbvGr"]
            kitchenabvgr = row["KitchenAbvGr"]
            kitchenqual = row["KitchenQual"]
            totrmsabvgrd = row["TotRmsAbvGrd"]
            functional = row["Functional"]
            fireplaces = row["Fireplaces"]
            fireplacequ = row["FireplaceQu"]
            garagetype = row["GarageType"]
            garageyrblt = row["GarageYrBlt"]
            garagefinish = row["GarageFinish"]
            garagecars = row["GarageCars"]
            garagearea = row["GarageArea"]
            garagequal = row["GarageQual"]
            garagecond = row["GarageCond"]
            paveddrive = row["PavedDrive"]
            wooddecksf = row["WoodDeckSF"]
            openporchsf = row["OpenPorchSF"]
            enclosedporch = row["EnclosedPorch"]
            threessnporch = row["3SsnPorch"]
            screenporch = row["ScreenPorch"]
            poolarea = row["PoolArea"]
            poolqc = row["PoolQC"]
            fence = row["Fence"]
            miscfeature = row["MiscFeature"]
            miscval = row["MiscVal"]
            mosold = row["MoSold"]
            yrsold = row["YrSold"]
            saletype = row["SaleType"]
            salecondition = row["SaleCondition"]

            data.append(
                {
                    "Id": nama_kpi,
                    "MSSubClass": mssubclass,
                    "MSZoning": mszoning,
                    "LotFrontage": lotfrontage,
                    "LotArea": lotarea,
                    "Street": street,
                    "Alley": alley,
                    "LotShape": lotshape,
                    "LandContour": landcontour,
                    "Utilities": utilities,
                    "LotConfig": lotconfig,
                    "LandSlope": landslope,
                    "Neighborhood": neighborhood,
                    "Condition1": condition1,
                    "Condition2": condition2,
                    "BldgType": bldgtype,
                    "HouseStyle": housestyle,
                    "OverallQual": overallqual,
                    "OverallCond": overallcond,
                    "YearBuilt": yearbuilt,
                    "YearRemodAdd": yearremodadd,
                    "RoofStyle": roofstyle,
                    "RoofMatl": roofmatl,
                    "Exterior1st": exterior1st,
                    "Exterior2nd": exterior2nd,
                    "MasVnrType": masvnrtype,
                    "MasVnrArea": masvnrarea,
                    "ExterQual": exterqual,
                    "ExterCond": extercond,
                    "Foundation": foundation,
                    "BsmtQual": bsmtqual,
                    "BsmtCond": bsmtcond,
                    "BsmtExposure": bsmtexposure,
                    "BsmtFinType1": bsmtfintype1,
                    "BsmtFinSF1": bsmtfinsf1,
                    "BsmtFinType2": bsmtfintype2,
                    "BsmtFinSF2": bsmtfinsf2,
                    "BsmtUnfSF": bsmtunfsf,
                    "TotalBsmtSF": totalbsmtsf,
                    "Heating": heating,
                    "HeatingQC": heatingqc,
                    "CentralAir": centralair,
                    "Electrical": electrical,
                    "1stFlrSF": firstflrsf,
                    "2ndFlrSF": secondflrsf,
                    "LowQualFinSF": lowqualfinsf,
                    "GrLivArea": grlivarea,
                    "BsmtFullBath": bsmtfullbath,
                    "BsmtHalfBath": bsmthalfbath,
                    "FullBath": fullbath,
                    "HalfBath": halfbath,
                    "BedroomAbvGr": bedroomabvgr,
                    "KitchenAbvGr": kitchenabvgr,
                    "KitchenQual": kitchenqual,
                    "TotRmsAbvGrd": totrmsabvgrd,
                    "Functional": functional,
                    "Fireplaces": fireplaces,
                    "FireplaceQu": fireplacequ,
                    "GarageType": garagetype,
                    "GarageYrBlt": garageyrblt,
                    "GarageFinish": garagefinish,
                    "GarageCars": garagecars,
                    "GarageArea": garagearea,
                    "GarageQual": garagequal,
                    "GarageCond": garagecond,
                    "PavedDrive": paveddrive,
                    "WoodDeckSF": wooddecksf,
                    "OpenPorchSF": openporchsf,
                    "EnclosedPorch": enclosedporch,
                    "3SsnPorch": threessnporch,
                    "ScreenPorch": screenporch,
                    "PoolArea": poolarea,
                    "PoolQC": poolqc,
                    "Fence": fence,
                    "MiscFeature": miscfeature,
                    "MiscVal": miscval,
                    "MoSold": mosold,
                    "YrSold": yrsold,
                    "SaleType": saletype,
                    "SaleCondition": salecondition,
                }
            )
    return data


# Route untuk dashboard
@app.route("/")
def dashboard():
    data = read_csv_file("Tugas Mandiri 080923 - data.csv")
    return render_template("index.html", data=data)


# Route untuk halaman filter
@app.route("/home")
def home():
    return render_template("index.html")


# Route untuk halaman EDA
@app.route("/eda")
def eda():
    return render_template("eda.html")

# Route untuk halaman EDA
@app.route("/teams")
def teams():
    return render_template("teams.html")

# Route untuk halaman Data
@app.route("/DATA")
def showData():
    data = read_csv_file("Tugas Mandiri 080923 - data.csv")
    return render_template("data.html", data=data)

# Route untuk halaman Index2
@app.route("/indx2")
def showIndex2():
    data = read_csv_file("Tugas Mandiri 080923 - data.csv")
    return render_template("indexdua.html")


# Route untuk menangani permintaan filter dan menampilkan hasil filter
@app.route("/filter_result", methods=["POST"])
def filter_result():
    sale_condition = request.form.get("sale_condition")

    # Baca data dari file CSV
    data = read_csv_file(
        "data.csv"
    )  # Ganti 'data.csv' dengan nama file CSV yang sesuai

    # Filter data berdasarkan Sale Condition yang dipilih
    filtered_data = [row for row in data if row["SaleCondition"] == sale_condition]

    return render_template(
        "filter_result.html", data=filtered_data, selected_condition=sale_condition
    )


if __name__ == "__main__":
    app.run(debug=True)
