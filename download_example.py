from report_downloader import ReportDownloader

# 实例化下载器 category为报告类型（年报、半年度报告、一季度报告、三季度报告、招股说明书）
# report_path为报告存储路径（默认为以报告类型为名称的文件夹）
downloader = ReportDownloader(category="年度报告")
# 若使用默认配置 则会在当前目录下创建“年度报告”文件夹，并开始下载所有上市公司2007-2022年的年度报告
# downloader.download()
stock_codes = ['600030', '000878', '300054', '603877', '300063']
downloader.download(start_year=2021,end_year=2021,stock_codes=stock_codes,file_type='pdf')