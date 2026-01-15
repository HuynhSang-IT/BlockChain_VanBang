import hre from "hardhat";

async function main() {
  // Lấy bản thiết kế
  const BangCap = await hre.ethers.getContractFactory("BangCap");

  console.log("Dang ket noi Cronos va deploy...");

  // Bắt đầu Deploy
  const hopDong = await BangCap.deploy();

  // Chờ mạng lưới xác nhận
  await hopDong.waitForDeployment();

  console.log("CHUC MUNG! Dia chi hop dong cua ban la:", hopDong.target);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});