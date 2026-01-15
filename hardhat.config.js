import "@nomicfoundation/hardhat-toolbox";
import dotenv from "dotenv";

// Nạp cấu hình bảo mật
dotenv.config();

/** @type import('hardhat/config').HardhatUserConfig */
export default {
  solidity: "0.8.24",
  networks: {
    cronos_testnet: {
      url: "https://evm-t3.cronos.org/",
      accounts: [process.env.PRIVATE_KEY],
      chainId: 338,
    },
  },
};